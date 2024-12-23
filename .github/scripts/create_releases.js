import { Octokit } from "@octokit/rest";
import fs from "fs";
import path from "path";
import { exec } from "child_process";
import util from "util";

const execAsync = util.promisify(exec);

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

const GITHUB_REPO = process.env.GITHUB_REPO;
if (!GITHUB_REPO) {
  console.error("GITHUB_REPO environment variable is required");
  process.exit(1);
}

const [owner, repo] = GITHUB_REPO.split("/");

const buildDir = path.join(process.cwd(), "build");

const getVersionDirectories = () => {
  return fs
    .readdirSync(buildDir, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .map((dirent) => dirent.name);
};

const zipDirectory = async (version) => {
  const sourceDir = path.join(buildDir, version);
  const zipPath = path.join(process.cwd(), `${version}.zip`);
  try {
    const { stdout, stderr } = await execAsync(
      `zip -r ${zipPath} ${sourceDir}`
    );
    if (stderr) {
      console.error(`Error zipping directory ${version}:`, stderr);
      throw new Error(stderr);
    }
    console.log(`Zipped ${sourceDir} to ${zipPath}`);
    return zipPath;
  } catch (error) {
    console.error(`Failed to zip directory ${version}:`, error);
    throw error;
  }
};

const deleteRelease = async (version) => {
  try {
    const releases = await octokit.repos.listReleases({
      owner,
      repo,
      per_page: 100,
    });

    const release = releases.data.find((r) => r.tag_name === version);
    if (release) {
      await octokit.repos.deleteRelease({
        owner,
        repo,
        release_id: release.id,
      });

      // Delete the tag
      await octokit.git.deleteRef({
        owner,
        repo,
        ref: `tags/${version}`,
      });

      console.log(`Deleted existing release and tag for version: ${version}`);
    } else {
      console.log(`No existing release found for version: ${version}`);
    }
  } catch (error) {
    console.error(`Error deleting release for version ${version}:`, error);
    throw error;
  }
};

const createRelease = async (version, zipPaths) => {
  try {
    const release = await octokit.repos.createRelease({
      owner,
      repo,
      tag_name: version,
      name: `Release ${version}`,
      body: `Automated release for version ${version}`,
      draft: false,
      prerelease: false,
    });

    for (const zipPath of zipPaths) {
      if (fs.existsSync(zipPath)) {
        await octokit.repos.uploadReleaseAsset({
          owner,
          repo,
          release_id: release.data.id,
          name: path.basename(zipPath),
          data: fs.createReadStream(zipPath),
        });
        console.log(
          `Uploaded asset: ${path.basename(zipPath)} to release ${version}`
        );
      } else {
        console.warn(`Zip file not found: ${zipPath}. Skipping upload.`);
      }
    }

    console.log(`Created release for version: ${version}`);
  } catch (error) {
    console.error(`Error creating release for version ${version}:`, error);
    throw error;
  }
};

const main = async () => {
  const versions = getVersionDirectories();
  for (const version of versions) {
    console.log(`Processing version: ${version}`);
    try {
      await deleteRelease(version);
      const zipPath = await zipDirectory(version);

      // Path to the zipped Live directory created by the GitHub Actions workflow
      const liveZipPath = path.join(buildDir, version, "Live.zip");

      await createRelease(version, [zipPath, liveZipPath]);

      // Optionally delete the zip files after upload
      // fs.unlinkSync(zipPath);
      // if (fs.existsSync(liveZipPath)) {
      //   fs.unlinkSync(liveZipPath);
      // }
      console.log(`Completed processing for version: ${version}\n`);
    } catch (error) {
      console.error(`Failed to process version ${version}:`, error);
    }
  }
};

main();
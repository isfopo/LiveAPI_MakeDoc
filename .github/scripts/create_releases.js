import { Octokit } from "@octokit/rest";
import fs from "fs";
import path from "path";
import { exec } from "child_process";
import util from "util";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const buildDir = join(__dirname, "../../build");

const execAsync = util.promisify(exec);

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

const GITHUB_REPO = process.env.GITHUB_REPO;
if (!GITHUB_REPO) {
  console.error("GITHUB_REPO environment variable is required");
  process.exit(1);
}

const [owner, repo] = GITHUB_REPO.split("/");

const getVersionDirectories = () => {
  return fs
    .readdirSync(buildDir, { withFileTypes: true })
    .filter((dirent) => dirent.isDirectory())
    .map((dirent) => dirent.name);
};

const zipDirectory = async (version) => {
  const sourceDir = path.join(buildDir, version, "Live");
  const zipPath = path.join(process.cwd(), version, `Live.zip`);

  // Ensure the source directory exists
  if (!fs.existsSync(sourceDir)) {
    console.error(`Source directory does not exist: ${sourceDir}`);
    throw new Error(`Source directory not found: ${sourceDir}`);
  }

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

const createRelease = async (version, zipPath) => {
  await deleteRelease(version);

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

    console.log(`Created release: ${release.data.name}`);

    // Check if zipPath exists before uploading
    if (fs.existsSync(zipPath)) {
      // Get the size of the file in bytes
      const stat = fs.statSync(zipPath);
      const fileSizeInBytes = stat.size;

      await octokit.repos.uploadReleaseAsset({
        owner,
        repo,
        release_id: release.data.id,
        name: path.basename(zipPath),
        data: fs.createReadStream(zipPath),
        headers: {
          "content-type": "application/zip",
          "content-length": fileSizeInBytes,
        },
      });

      console.log(
        `Uploaded asset: ${path.basename(zipPath)} to release ${version}`
      );
    } else {
      console.warn(`Zip file not found: ${zipPath}. Skipping upload.`);
    }

    console.log(`Created release for version: ${version}`);
  } catch (error) {
    console.error(`Error creating release for version ${version}:`, error);
    throw error;
  }
};

(async () => {
  for (const version of getVersionDirectories()) {
    console.log(`Processing version: ${version}`);
    try {
      await createRelease(version, await zipDirectory(version));

      console.log(`Completed processing for version: ${version}\n`);
    } catch (error) {
      console.error(`Failed to process version ${version}:`, error);
    }
  }
})();

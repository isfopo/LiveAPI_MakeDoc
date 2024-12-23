import { Octokit } from "@octokit/rest";
import fs from "fs";
import { join, dirname, basename } from "path";
import { exec } from "child_process";
import { promisify } from "util";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const buildDir = join(__dirname, "../../build");

const execAsync = promisify(exec);

const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

const GITHUB_REPO = process.env.GITHUB_REPO;
if (!GITHUB_REPO) {
  console.error("GITHUB_REPO environment variable is required");
  process.exit(1);
}

const [owner, repo] = GITHUB_REPO.split("/");

const getVersionDirectories = (buildDir) => {
  if (!fs.existsSync(buildDir)) {
    console.error(`Build directory does not exist: ${buildDir}`);
    process.exit(1);
  }

  return fs
    .readdirSync(buildDir, { withFileTypes: true })
    .filter(
      (dirent) => dirent.isDirectory() && /^\d+\.\d+\.\d+$/.test(dirent.name)
    )
    .map((dirent) => dirent.name);
};

// Function to zip a directory
const zipDirectory = async (version) => {
  const sourceDir = join(buildDir, version); // Path to the version folder
  const zipPath = join(buildDir, `${version}.zip`); // Destination ZIP path in build/version.zip

  console.log(`\nProcessing version: ${version}`);
  console.log(`Source Directory: ${sourceDir}`);
  console.log(`Destination Zip Path: ${zipPath}`);

  // Verify that the source directory exists
  if (!fs.existsSync(sourceDir)) {
    console.error(`Source directory does not exist: ${sourceDir}`);
    throw new Error(`Source directory not found: ${sourceDir}`);
  }

  try {
    // Change into the source directory and zip its contents
    const { stdout, stderr } = await execAsync(
      `cd "${sourceDir}" && zip -r "${zipPath}" .`
    );

    if (stderr && stderr.trim() !== "") {
      console.error(`Error zipping directory ${version}:`, stderr);
      throw new Error(stderr);
    }

    console.log(`Successfully zipped contents of ${sourceDir} to ${zipPath}`);
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

// Function to explicitly update a release to set draft: false (publish the release)
const updateReleaseToPublish = async (release_id) => {
  try {
    const updatedRelease = await octokit.repos.updateRelease({
      owner,
      repo,
      release_id,
      draft: false, // Set draft to false to publish
    });

    console.log(`Updated release ID ${release_id} to published.`);
    return updatedRelease;
  } catch (error) {
    console.error(`Error updating release ID ${release_id} to publish:`, error);
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

    // If release is still a draft (shouldn't be), explicitly publish it
    if (release.data.draft) {
      console.log(`Release ${version} is still a draft. Publishing it.`);
      await updateReleaseToPublish(release.data.id);
      // Optionally, refetch the release to confirm
      const updatedRelease = await octokit.repos.getRelease({
        owner,
        repo,
        release_id: release.data.id,
      });
      console.log(
        `Draft status after publishing: ${updatedRelease.data.draft}`
      );
    }

    // Check if zipPath exists before uploading
    if (fs.existsSync(zipPath)) {
      // Get the size of the file in bytes
      const stat = fs.statSync(zipPath);
      const fileSizeInBytes = stat.size;

      await octokit.repos.uploadReleaseAsset({
        owner,
        repo,
        release_id: release.data.id,
        name: basename(zipPath),
        data: fs.createReadStream(zipPath),
        headers: {
          "content-type": "application/zip",
          "content-length": fileSizeInBytes,
        },
      });

      console.log(`Uploaded asset: ${basename(zipPath)} to release ${version}`);
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
  for (const version of getVersionDirectories(buildDir)) {
    console.log(`Processing version: ${version}`);
    try {
      await createRelease(version, await zipDirectory(version));

      console.log(`Completed processing for version: ${version}\n`);
    } catch (error) {
      console.error(`Failed to process version ${version}:`, error);
    }
  }
})();

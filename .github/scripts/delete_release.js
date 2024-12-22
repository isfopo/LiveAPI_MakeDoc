import { Octokit } from "@octokit/rest";

const deleteRelease = async () => {
  const tag = `${process.env.VERSION}`;
  const [owner, repo] = process.env.GITHUB_REPO.split("/");
  const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

  try {
    const releases = await octokit.repos.listReleases({
      owner,
      repo,
      per_page: 100,
    });

    const release = releases.data.find((r) => r.tag_name === tag);
    if (release) {
      await octokit.repos.deleteRelease({
        owner,
        repo,
        release_id: release.id,
      });

      console.log(`Deleted existing release and tag: ${tag}`);
    } else {
      console.log(`No existing release found for tag: ${tag}`);
    }
  } catch (error) {
    console.error(`Error deleting release: ${error}`);
    process.exit(1);
  }
};

deleteRelease();

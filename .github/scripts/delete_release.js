const { Octokit } = require("@octokit/rest");

const deleteRelease = async () => {
  const tag = `v${process.env.VERSION}`;
  const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });
  console.log(`Attempting to delete release for tag: ${tag}`);
  console.log(`Fetching releases for repository: ${process.env.GITHUB_REPO}`);

  try {
    const releases = await octokit.repos.listReleases({
      owner: process.env.GITHUB_OWNER,
      repo: process.env.GITHUB_REPO,
      per_page: 100,
    });

    const release = releases.data.find((r) => r.tag_name === tag);
    if (release) {
      await octokit.repos.deleteRelease({
        owner: process.env.GITHUB_OWNER,
        repo: process.env.GITHUB_REPO,
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

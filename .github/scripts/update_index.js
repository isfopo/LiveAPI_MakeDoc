import { readFile, readdir, writeFile } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const buildDir = join(__dirname, "../../build");
const webDir = join(__dirname, "../../web");

const templatePath = join(webDir, "index.html");
const stylesPath = join(webDir, "styles.css");
const indexDest = join(buildDir, "index.html");
const stylesDest = join(buildDir, "index.html");

readFile(templatePath, "utf8", (err, templateData) => {
  if (err) {
    console.error("Error reading template file:", err);
    process.exit(1);
  }

  readdir(buildDir, { withFileTypes: true }, (err, files) => {
    if (err) {
      console.error("Error reading build directory:", err);
      process.exit(1);
    }

    // Filter directories that match semantic versioning (e.g., 12.1.0)
    const versionDirs = files
      .filter((dir) => dir.isDirectory() && /^\d+\.\d+\.\d+$/.test(dir.name))
      .map((dir) => dir.name)
      .sort((a, b) => {
        const [aMajor, aMinor, aPatch] = a.split(".").map(Number);
        const [bMajor, bMinor, bPatch] = b.split(".").map(Number);
        if (aMajor !== bMajor) return aMajor - bMajor;
        if (aMinor !== bMinor) return aMinor - bMinor;
        return aPatch - bPatch;
      });

    // Generate HTML list items for each version
    const listItems = versionDirs
      .map((version) => {
        return `<li>
          <a href="${version}/Live.xml">Live Version ${version}</a> - <a href="https://github.com/isfopo/LiveAPI_MakeDoc/releases/download/${version}/${version}.zip">Download</a>
        </li>`;
      })
      .join("\n");

    // Replace the placeholder with the generated list items
    const updatedContent = templateData.replace(
      "<!-- VERSIONS_PLACEHOLDER -->",
      listItems
    );

    // Write the updated content to index.html
    writeFile(indexDest, updatedContent, (writeErr) => {
      if (writeErr) {
        console.error("Error writing to index.html:", writeErr);
        process.exit(1);
      }
      console.log(
        "build/index.html has been successfully updated with available versions."
      );
    });
  });
});

readFile(stylesPath, "utf8", (err, content) => {
  if (err) {
    console.error("Error reading template file:", err);
    process.exit(1);
  }
  // Write the updated content to styles.css
  writeFile(stylesDest, content, (writeErr) => {
    if (writeErr) {
      console.error("Error writing to styles.css:", writeErr);
      process.exit(1);
    }
    console.log(
      "build/styles.css has been successfully updated at" + stylesDest
    );
  });
});

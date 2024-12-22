import fs from "fs";
import path from "path";
import { compile } from "svelte/compiler";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const buildDir = path.join(__dirname, "../../build");
const versionsPath = path.join(__dirname, "../../web/versions.json"); // Path to write versions.json
const appPath = path.join(__dirname, "../../web/src/App.svelte");
const indexTemplatePath = path.join(
  __dirname,
  "../../.github/scripts/index_template.html"
);
const outputIndexPath = path.join(buildDir, "index.html");

// Function to compile Svelte component
function compileSvelte() {
  const appContent = fs.readFileSync(appPath, "utf-8");
  const compiled = compile(appContent, {
    name: "App",
    dev: false,
  });
  return compiled.js.code;
}

// Function to generate versions.json
function generateVersions() {
  fs.readdir(buildDir, { withFileTypes: true }, (err, files) => {
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
        return bPatch - aPatch;
      });

    // Write versions.json
    fs.writeFile(
      versionsPath,
      JSON.stringify(versionDirs, null, 2),
      (writeErr) => {
        if (writeErr) {
          console.error("Error writing versions.json:", writeErr);
          process.exit(1);
        }
        console.log(
          "web/versions.json has been successfully created with available versions."
        );
      }
    );
  });
}

// Function to update index.html with compiled Svelte and versions
function updateIndexHtml() {
  const compiledSvelte = compileSvelte();

  fs.readFile(indexTemplatePath, "utf-8", (err, template) => {
    if (err) {
      console.error("Error reading index_template.html:", err);
      process.exit(1);
    }

    // Replace VERSIONS_PLACEHOLDER with versions data
    fs.readFile(versionsPath, "utf-8", (versionsErr, versionsData) => {
      if (versionsErr) {
        console.error("Error reading versions.json:", versionsErr);
        process.exit(1);
      }

      const versions = JSON.parse(versionsData);
      const versionsList = versions
        .map((version) => `<li>${version}</li>`)
        .join("\n          ");

      const updatedHtml = html`<!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>LiveAPI Versions</title>
        </head>        
          <script>
            ${compiledSvelte}
            new App({
              target: document.body
            });
          </script>
        </body>
      </html>`;

      fs.writeFile(outputIndexPath, updatedHtml, (writeErr) => {
        if (writeErr) {
          console.error("Error writing index.html:", writeErr);
          process.exit(1);
        }
        console.log(
          "build/index.html has been successfully created with compiled Svelte code."
        );
      });
    });
  });
}

// Execute functions
generateVersions();
updateIndexHtml();

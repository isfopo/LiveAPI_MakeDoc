#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const process = require("process");
const diff = require("diff");

// Retrieve arguments for current and previous versions
const currentVersion = process.env.CURRENT_VERSION;
const previousVersion = process.env.PREVIOUS_VERSION;

// Define the base build directory
const BUILD_DIR = path.join(__dirname, "../../build");

// Function to read a file's content
const readFileContent = (version) => {
  const filePath = path.join(BUILD_DIR, version, "Live.xml");
  if (!fs.existsSync(filePath)) {
    throw new Error(`Live.xml not found for version: ${version}`);
  }
  return fs.readFileSync(filePath, "utf-8");
};

// Function to escape XML special characters
const escapeXml = (unsafe) => {
  return unsafe.replace(/[<>&'"]/g, (c) => {
    switch (c) {
      case "<":
        return "<";
      case ">":
        return ">";
      case "&":
        return "&amp;";
      case "'":
        return "&apos;";
      case '"':
        return '"';
    }
  });
};

// Function to compute the diff between two versions and generate XML
const computeDiffXml = (prevContent, currContent) => {
  const differences = diff.diffLines(prevContent, currContent);
  let xmlContent = '<?xml version="1.0" encoding="UTF-8"?>\n<diff>\n';

  differences.forEach((part) => {
    const type = part.added ? "added" : part.removed ? "removed" : "unchanged";
    part.value.split("\n").forEach((line) => {
      if (line.trim() !== "") {
        // Ignore empty lines
        xmlContent += `  <change type="${type}">${escapeXml(line)}</change>\n`;
      }
    });
  });

  xmlContent += "</diff>";
  return xmlContent;
};

// Main execution block
try {
  if (!currentVersion) {
    throw new Error("Current version number is required.");
  }

  let xmlContent = "";

  if (!previousVersion) {
    console.log(
      "No previous version provided. Using entire Live.xml as release notes."
    );
    const currentContent = readFileContent(currentVersion);
    xmlContent = `<?xml version="1.0" encoding="UTF-8"?>\n<diff>\n  <change type="unchanged">${escapeXml(
      currentContent
    )}</change>\n</diff>`;
  } else {
    try {
      const previousContent = readFileContent(previousVersion);
      const currentContent = readFileContent(currentVersion);
      xmlContent = computeDiffXml(previousContent, currentContent);
    } catch (err) {
      console.log("Previous Live.xml not found.");
      xmlContent =
        '<?xml version="1.0" encoding="UTF-8"?>\n<diff>\n  <change type="unchanged">No changes found in the previous version</change>\n</diff>';
    }
  }

  // Define the path for the XML output
  const xmlOutputPath = path.join(BUILD_DIR, currentVersion, "diff.xml");

  // Write the XML content to the file
  fs.writeFileSync(xmlOutputPath, xmlContent, "utf-8");
  console.log(`Diff XML has been written to ${xmlOutputPath}`);

  // Optionally, write the XML path to GITHUB_OUTPUT
  if (process.env.GITHUB_OUTPUT) {
    fs.appendFileSync(
      process.env.GITHUB_OUTPUT,
      `diff_xml_path<<EOF\n${xmlOutputPath}\nEOF\n`
    );
  } else {
    console.log("GITHUB_OUTPUT environment variable is not defined.");
    console.log("Diff XML Path:\n", xmlOutputPath);
  }
} catch (error) {
  console.error("Error:", error.message);
  process.exit(1);
}

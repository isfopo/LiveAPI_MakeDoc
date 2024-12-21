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

// Function to compute the diff between two versions
const computeDiff = (prevContent, currContent) => {
  const differences = diff.diffLines(prevContent, currContent);
  if (differences.length === 0) {
    return "No changes in Live.xml since the previous release.";
  }

  let diffContent = "";
  differences.forEach((part) => {
    const prefix = part.added ? "+" : part.removed ? "-" : " ";
    // Split the diff into lines and prepend the prefix
    part.value.split("\n").forEach((line) => {
      if (line.trim() !== "") {
        // Ignore empty lines
        diffContent += `${prefix} ${line}\n`;
      }
    });
  });

  return diffContent;
};

// Main execution block
try {
  if (!currentVersion) {
    throw new Error("Current version number is required.");
  }

  let diffContent = "";

  if (!previousVersion) {
    console.log(
      "No previous version provided. Using entire Live.xml as release notes."
    );
    const currentContent = readFileContent(currentVersion);
    diffContent = currentContent;
  } else {
    try {
      const previousContent = readFileContent(previousVersion);
      const currentContent = readFileContent(currentVersion);
      diffContent = computeDiff(previousContent, currentContent);
    } catch (err) {
      console.log(
        "Previous Live.xml not found. Using entire Live.xml as release notes."
      );
      const currentContent = readFileContent(currentVersion);
      diffContent = currentContent;
    }
  }

  // Write the diff content to GITHUB_OUTPUT for use in subsequent steps
  if (process.env.GITHUB_OUTPUT) {
    fs.appendFileSync(
      process.env.GITHUB_OUTPUT,
      `diff_content<<EOF\n${diffContent}\nEOF\n`
    );
  } else {
    console.log("GITHUB_OUTPUT environment variable is not defined.");
    console.log("Diff Content:\n", diffContent);
  }
} catch (error) {
  console.error("Error:", error.message);
  process.exit(1);
}

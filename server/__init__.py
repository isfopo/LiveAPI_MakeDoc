import os
import re
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():

    # Define the build folder path (relative to app.py)
    build_folder = './server/build'

    # Regex for a basic semantic version format: MAJOR.MINOR.PATCH
    # Each component must be a non-negative integer, without leading zeros for numbers > 0.
    # E.g., '1.0.0', '12.3.45', '0.1.2' are valid. '01.0.0' is not.
    semver_component_regex = r'(?:0|[1-9]\d*)'
    semver_regex = rf'^{semver_component_regex}\.{semver_component_regex}\.{semver_component_regex}$'

    semver_dirs = []
    try:
        # Get all entries (files and directories) in the build folder
        all_entries = os.listdir(build_folder)
        app.logger.info(f"Found {len(all_entries)} entries in the build folder.")
        for entry in all_entries:
            full_path = os.path.join(build_folder, entry)
            # Check if the entry is a directory
            if os.path.isdir(full_path):
                # Check if the directory name matches the semantic version pattern
                if re.match(semver_regex, entry):
                    semver_dirs.append(entry)
    except FileNotFoundError as e:
        print(e)
        # If the build folder does not exist, semver_dirs remains an empty list.
        # This handles the absence of the folder gracefully without crashing.
        pass

    # At this point, 'semver_dirs' contains the list of directory names
    # from the 'build' folder that are valid semantic versions.
    # Example: ['1.0.0', '1.2.3', '2.0.0']
    return render_template('index.html', versions=semver_dirs)

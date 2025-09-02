import os
import re
from flask import Flask, render_template, make_response


semver_component_regex = r'(?:0|[1-9]\d*)'
semver_regex = rf'^{semver_component_regex}\.{semver_component_regex}\.{semver_component_regex}$'
build_folder = './build'

app = Flask(__name__)

@app.route("/")
def index():

    print("Fetching version list...")
    semver_dirs = []

    try:
        all_entries = os.listdir(build_folder)
        app.logger.info(f"Found {len(all_entries)} entries in the build folder.")
        for entry in all_entries:
            full_path = os.path.join(build_folder, entry)
            if os.path.isdir(full_path):
                if re.match(semver_regex, entry):
                    semver_dirs.append(entry)
    except FileNotFoundError as e:
        print(e)
        pass

    return make_response(render_template('index.html', data={'versions': semver_dirs}))

@app.route("/<string:version>")
def version(version):
    # Check if the version is a valid semantic version
    if not re.match(semver_regex, version):
        return f"Invalid version: {version}", 400

    try:
        version_path = os.path.join(build_folder, version)
        xml_file_path = os.path.join(version_path, 'Live.xml')

        # Ensure the directory for the version exists
        if not os.path.isdir(version_path):
            raise FileNotFoundError(f"Version directory not found for {version}")

        xml_content = ""
        # Attempt to open and read the version-specific XML file
        with open(xml_file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read() # Read the content of the XML file

        resp = make_response(xml_content, 200)
        resp.headers['Content-Type'] = 'application/xml'
        return resp

    except FileNotFoundError:
        # If the specified XML file or version directory does not exist, return a 404 Not Found error
        return f"Version {version} or its Live.xml file not found", 404

if __name__ == '__main__':
    app.run()

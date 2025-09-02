import os
import re
from flask import Flask, render_template, make_response
from flask_restful import Api, Resource


semver_component_regex = r'(?:0|[1-9]\d*)'
semver_regex = rf'^{semver_component_regex}\.{semver_component_regex}\.{semver_component_regex}$'
build_folder = './server/build'

app = Flask(__name__)
api = Api(app)

class VersionListResource(Resource):
    def get(self):

        # Define the build folder path (relative to app.py)

        # Regex for a basic semantic version format: MAJOR.MINOR.PATCH
        # Each component must be a non-negative integer, without leading zeros for numbers > 0.
        # E.g., '1.0.0', '12.3.45', '0.1.2' are valid. '01.0.0' is not.

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
        return make_response(render_template('index.html', data={'versions': semver_dirs}))

class VersionResource(Resource):
    def get(self, version):
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


api.add_resource(VersionListResource, '/')
api.add_resource(VersionResource, '/<string:version>')

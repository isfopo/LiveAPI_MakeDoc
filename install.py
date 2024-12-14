"""
This script is designed to "install" your Remote Script to Ableton Live.
Essentally all that is to move the folder names 'src' to the appropriate
location on your computer for Live to recognize and compile it to be
used in a Live set.

Once this script has run, start or restart Ableton and your Remote Script
should be available to you in your Midi preferences as one of the options
for a control surface. This process will have to be run again when you
have made changes in your code to see those changes in your control surface.

This script only works for Live 11 because it relocates the folder to the
User Library. If your User Library is in a different location than the
standard installation you will need to either need to change the path in
the script or pass in the path to your User Library as an argument using
the `--path` flag. Pass in the full path, including "User Library".

This script also takes a guess at your username for the path. If this guess
is incorrect or there is some kind of error, try adding your username with
the `--user` flag.

The `--name` flag can be used if you would like the name of the output folder
to be different than the name of the directory the project is in.

If you have changed the name of your src folder, then it will need to be
changed here as well.
"""

import os
import shutil
import getpass
import argparse
import platform

USERLIBWIN = "C:\\Users\\{user}\\Documents\\Ableton\\User Library"
USERLIBMAC = "/Users/{user}/Music/Ableton/User Library"

parser = argparse.ArgumentParser(description="Install remote script")
parser.add_argument("--path", "-path to User Library folder", required=False)
parser.add_argument("--user", "-your account username", required=False)
parser.add_argument("--name", "-name of output folder", required=False)

args = parser.parse_args()

currentDir = os.getcwd()
srcDir = os.path.join(currentDir, "src")

user = args.user or getpass.getuser()

userScriptsPath = os.path.join(
    args.path
    or (USERLIBWIN if platform.system() == "Windows" else USERLIBMAC).format(user=user),
    "Remote Scripts",
)

outputDir = os.path.join(userScriptsPath, args.name or os.path.basename(currentDir))

if os.path.isdir(outputDir):
    shutil.rmtree(outputDir)

shutil.copytree(srcDir, outputDir)

print(
    """
    Your code was successfully moved to your User Library folder.
    Restart Ableton to see your Remote Script.
"""
)

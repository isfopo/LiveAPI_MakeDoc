# Releases

Because the output of this documentation and stub is dependant on the version of this software and the version of Ableton Live, releases to this repository are tagged with the version of Ableton Live they are compatible with. Changes to this software are made in the `develop` branch and merged into the `master` branch when a new release is ready, then all available versions of Live API documentation are updated at the same time.

## Generating Docs

Generating docs happens dynamically in the python runtime of Ableton Live via a remote script. This script must be installed and the intended version of Live API documentation must be downloaded and installed in order to generate the docs and the stub.

### Installing the Script

After cloning this repository, install the script by running the following command from the root of the repository:

```bash
python3 install.py --name MakeDoc_Release --mode release
```

There is a shortcut for this command in the `justfile` of this project which can be run if [just](https://github.com/casey/just) is installed.

### Generating the Docs and Stub

To run the remote script and generate the docs open Ableton Live, go to Preferences > Link, Tempo and MIDI, and select `MakeDoc Release` in the "Control Surface" dropdown.

Doing this will generate the docs and stub for the version of Live API that is currently installed and place them in the `release` folder of this repository under the corresponding version tag.

###

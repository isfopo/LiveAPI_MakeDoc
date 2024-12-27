# API_MakeDoc

This set of Python scripts will generate Live API documentation in XML format, based on realtime inspection of the Live module. Compatible with Live 8.1 & higher, on PC or mac.

To run, first drop the API_LiveDoc folder into Ableton's MIDI Remote Scripts directory:

MAC OS X -> /Applications/Live 8.x OS X/Live.app/Contents/App-Resources/MIDI Remote Scripts/
PC -> C:\Program Files\Ableton\Live 8.x\Resources\MIDI Remote Scripts\

Next, select "API_MakeDoc" from the MIDI Preferences dialog, then reset immediately to "None" (there is no need to close the dialog first). Two files will be written to the userhome directory: Live.xml and Live.css (sample output is included in the \_Sample_Output directory). To locate the userhome directory:

MAC OS X -> click the Home icon in the Finder toolbar
PC -> C:\Documents and Settings\username\

Open Live.xml in a web browser to view the API documentation.

## Usage

### Manual Installation

Dropping into Remote script folder

### Usage as a Submodule

How to use in another project or repository as a submodule

## Build andRelease

For releases, see the [Build and Release](https://github.com/isfopo/LiveAPI_MakeDoc/build) page.

## DISCLAIMER

THESE FILES ARE PROVIDED AS-IS, WITHOUT ANY WARRANTY, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO FITNESS FOR ANY PARTICULAR PURPOSE.

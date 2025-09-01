# type: ignore
from types import ModuleType

class Application(ModuleType):
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    class Application(object):
"""This class represents the Live application."""
        class View(object):
"""This class represents the view aspects of the Live application."""
            class NavDirection(object):
"""None"""
    class ControlDescription(object):
"""Describes a control present in a control surface proxy"""
    class ControlDescriptionVector(object):
"""A container for returning control descriptions."""
    class ControlSurfaceProxy(object):
"""Represents a control surface running in a different process. For use by M4L"""
    class MessageButtons(object):
"""Specifies the characteristics of the message box, e.g. which buttons to show."""
    class PushDialogType(object):
"""Specifies the dialog type for Push."""
    class UnavailableFeature(object):
"""None"""
    class UnavailableFeatureVector(object):
"""A container for returning unavailable features."""
    class Variants(object):
"""Holds strings representing what type of Live is running."""
class Base(ModuleType):
    @staticmethod
    @staticmethod
    @staticmethod
    class FloatVector(object):
"""A simple container for returning floats from Live."""
    class IntU64Vector(object):
"""A simple container for returning unsigned long integers from Live."""
    class IntVector(object):
"""A simple container for returning integers from Live."""
    class LimitationError(object):
"""None"""
    class ObjectVector(object):
"""A simple read only container for returning python objects."""
    class StringVector(object):
"""A simple container for returning strings from Live."""
    class Text(object):
"""A translatable, immutable string."""
    class Timer(object):
"""A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer."""
    class Vector(object):
"""A simple read only container for returning objects from Live."""
class Browser(ModuleType):
    class Browser(object):
"""This class represents the live browser data base."""
    class BrowserItem(object):
"""This class represents an item of the browser hierarchy."""
    class BrowserItemIterator(object):
"""This class iterates over children of another BrowserItem."""
    class BrowserItemVector(object):
"""A container for returning browser items from Live."""
    class FilterType(object):
"""None"""
    class Relation(object):
"""None"""
class CcControlDevice(ModuleType):
    class CcControlDevice(object):
"""This class represents a CcControl device."""
        class View(object):
"""Representing the view aspects of a device."""
class Chain(ModuleType):
    class Chain(object):
"""This class represents a group device chain in Live."""
class ChainMixerDevice(ModuleType):
    class ChainMixerDevice(object):
"""This class represents a Chain's Mixer Device in Live, which gives you
access to the Volume, Panning, and Send properties of a Chain."""
class Clip(ModuleType):
    class AutomationEnvelope(object):
"""Describes parameter automation per clip."""
    class Clip(object):
"""This class represents a Clip in Live. It can be either an Audio
Clip or a MIDI Clip, in an Arrangement or the Session, depending
on the Track (Slot) it lives in."""
        class View(object):
"""Representing the view aspects of a Clip."""
    class ClipLaunchQuantization(object):
"""None"""
    class GridQuantization(object):
"""None"""
    class LaunchMode(object):
"""None"""
    class MidiNote(object):
"""An object representing a MIDI Note"""
    class MidiNoteSpecification(object):
"""An object specifying the data for creating a MIDI note. To be used with the 
add_new_notes function."""
    class MidiNoteVector(object):
"""A container for holding MIDI notes from Live."""
    class WarpMarker(object):
"""This class represents a WarpMarker type."""
    class WarpMarkerVector(object):
"""A container for returning warp markers from Live."""
    class WarpMode(object):
"""None"""
class ClipSlot(ModuleType):
    class ClipSlot(object):
"""This class represents an entry in Lives Session view matrix."""
    class ClipSlotPlayingState(object):
""""""
class CompressorDevice(ModuleType):
    class CompressorDevice(object):
"""This class represents a Compressor device."""
        class View(object):
"""Representing the view aspects of a device."""
class Conversions(ModuleType):
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    class AudioToMidiType(object):
"""None"""
class Device(ModuleType):
    class ATimeableValueVector(object):
"""None"""
    class Device(object):
"""This class represents a MIDI or Audio DSP-Device in Live."""
        class View(object):
"""Representing the view aspects of a device."""
    class DeviceType(object):
"""The type of the device."""
class DeviceIO(ModuleType):
    class DeviceIO(object):
"""This class represents a specific input or output bus of a device."""
class DeviceParameter(ModuleType):
    class AutomationState(object):
"""None"""
    class DeviceParameter(object):
"""This class represents a (automatable) parameter within a MIDI or
Audio DSP-Device."""
    class ParameterState(object):
"""None"""
class DriftDevice(ModuleType):
    class DriftDevice(object):
"""This class represents a Drift device."""
        class View(object):
"""Representing the view aspects of a device."""
class DrumCellDevice(ModuleType):
    class DrumCellDevice(object):
"""This class represents a DrumCell device."""
        class View(object):
"""Representing the view aspects of a device."""
class DrumChain(ModuleType):
    class DrumChain(object):
"""This class represents a drum group device chain in Live."""
class DrumPad(ModuleType):
    class DrumPad(object):
"""This class represents a drum group device pad in Live."""
class Eq8Device(ModuleType):
    class EditMode(object):
"""None"""
    class Eq8Device(object):
"""This class represents an Eq8 device."""
        class View(object):
"""Representing the view aspects of an Eq8 device."""
    class GlobalMode(object):
"""None"""
class Groove(ModuleType):
    class Base(object):
"""None"""
    class Groove(object):
"""This class represents a groove in Live."""
class GroovePool(ModuleType):
    class GroovePool(object):
"""This class represents the groove pool in Live."""
class HybridReverbDevice(ModuleType):
    class HybridReverbDevice(object):
"""This class represents a Hybrid Reverb device."""
        class View(object):
"""Representing the view aspects of a device."""
class Licensing(ModuleType):
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    class ProgressDialog(object):
"""A modal dialog showing a message and a progress animation."""
    class PythonLicensingBridge(object):
"""Interface to the internal licensing services."""
    class StartupDialogServes as an entry point for the user to authorize Live on first launch.(object):
"""None"""
    class TrialContext(object):
"""None"""
    class UnlockStatus(object):
"""Returns relevant information after unlock"""
class Listener(ModuleType):
    class ListenerHandle(object):
"""This class represents a Python listener when connected to a Live property."""
    class ListenerVector(object):
"""A read only container for accessing a list of listeners."""
class LomObject(ModuleType):
    class LomObject(object):
"""this is the base class for an object that is accessible via the LOM"""
class LooperDevice(ModuleType):
    class LooperDevice(object):
"""This class represents a Looper device."""
        class View(object):
"""Representing the view aspects of a device."""
class MaxDevice(ModuleType):
    class MaxDevice(object):
"""This class represents a Max for Live device."""
        class View(object):
"""Representing the view aspects of a device."""
class MeldDevice(ModuleType):
    class MeldDevice(object):
"""This class represents a Meld device."""
        class View(object):
"""Representing the view aspects of a device."""
class MidiMap(ModuleType):
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    class CCFeedbackRule(object):
"""Structure to define feedback properties of MIDI mappings."""
    class MapMode(object):
"""None"""
    class NoteFeedbackRule(object):
"""Structure to define feedback properties of MIDI mappings."""
    class PitchBendFeedbackRule(object):
"""Structure to define feedback properties of MIDI mappings."""
class MixerDevice(ModuleType):
    class MixerDevice(object):
"""This class represents a Mixer Device in Live, which gives you
access to the Volume and Panning properties of a Track."""
        class crossfade_assignments(object):
"""None"""
        class panning_modes(object):
"""None"""
class PluginDevice(ModuleType):
    class PluginDevice(object):
"""This class represents a plugin device."""
        class View(object):
"""Representing the view aspects of a device."""
class RackDevice(ModuleType):
    class RackDevice(object):
"""This class represents a Rack device."""
        class View(object):
"""Representing the view aspects of a rack device."""
class RoarDevice(ModuleType):
    class RoarDevice(object):
"""This class represents a Roar device."""
        class View(object):
"""Representing the view aspects of a device."""
class Sample(ModuleType):
    class Sample(object):
"""This class represents a sample file loaded into a Simpler instance."""
    class SlicingBeatDivision(object):
"""None"""
    class SlicingStyle(object):
"""None"""
    class TransientLoopMode(object):
"""None"""
class Scene(ModuleType):
    class Scene(object):
"""This class represents an series of ClipSlots in Lives Sessionview matrix."""
class ShifterDevice(ModuleType):
    class ShifterDevice(object):
"""This class represents a Shifter device."""
        class View(object):
"""Representing the view aspects of a device."""
class SimplerDevice(ModuleType):
    @staticmethod
    class PlaybackMode(object):
"""None"""
    class SimplerDevice(object):
"""This class represents a Simpler device."""
        class View(object):
"""Representing the view aspects of a simpler device."""
    class SlicingPlaybackMode(object):
"""None"""
class Song(ModuleType):
    @staticmethod
    class BeatTime(object):
"""Represents a Time, splitted into Bars, Beats, SubDivision and Ticks."""
    class CaptureDestination(object):
"""The destination for MIDI capture."""
    class CaptureMode(object):
"""The capture mode that is used for capture and insert scene."""
    class CuePoint(object):
"""Represents a 'Marker' in the arrangement."""
    class Quantization(object):
"""None"""
    class RecordingQuantization(object):
"""None"""
    class SessionRecordStatus(object):
"""None"""
    class SmptTime(object):
"""Represents a Time, split into Hours, Minutes, Seconds and Frames.
The frame type must be specified when calling a function that returns
a SmptTime."""
    class Song(object):
"""This class represents a Live set."""
        class View(object):
"""Representing the view aspects of a Live document: The Session and Arrangerview."""
    class TimeFormat(object):
"""None"""
class SpectralResonatorDevice(ModuleType):
    class SpectralResonatorDevice(object):
"""This class represents a Spectral Resonator device."""
        class View(object):
"""Representing the view aspects of a device."""
class Track(ModuleType):
    class DeviceContainer(object):
"""This class is a common super class of Track and Chain"""
    class DeviceInsertMode(object):
"""None"""
    class RoutingChannel(object):
"""This class represents a routing channel."""
    class RoutingChannelLayout(object):
"""None"""
    class RoutingChannelVector(object):
"""A container for returning routing channels from Live."""
    class RoutingType(object):
"""This class represents a routing type."""
    class RoutingTypeCategory(object):
"""None"""
    class RoutingTypeVector(object):
"""A container for returning routing types from Live."""
    class Track(object):
"""This class represents a track in Live. It can be either an Audio 
track, a MIDI Track, a Return Track or the Main track. The Main 
Track and at least one Audio or MIDI track will be always present.
Return Tracks are optional."""
        class View(object):
"""Representing the view aspects of a Track."""
        class monitoring_states(object):
"""None"""
class TuningSystem(ModuleType):
    class PitchClassAndOctave(object):
"""This class represents a PitchClassAndOctave type."""
    class ReferencePitch(object):
"""This class represents a ReferencePitch type."""
    class TuningSystem(object):
"""Represents a Tuning System and its properties."""
class WavetableDevice(ModuleType):
    class EffectMode(object):
"""None"""
    class FilterRouting(object):
"""None"""
    class ModulationSource(object):
"""None"""
    class UnisonMode(object):
"""None"""
    class VoiceCount(object):
"""None"""
    class Voicing(object):
"""None"""
    class WavetableDevice(object):
"""This class represents a Wavetable device."""
        class View(object):
"""Representing the view aspects of a device."""

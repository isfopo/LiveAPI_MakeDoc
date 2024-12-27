# type: ignore
from types import ModuleType
"""Stub generated for Ableton Version  12.1.5"""


class Application(ModuleType):
    pass

    @staticmethod
    def combine_apcs():
        """
        Returns true if multiple APCs should be combined.

 C++ signature :
  bool combine_apcs()
        """
        pass

    @staticmethod
    def encrypt_challenge(dongle1: int, dongle2: int, key_index: int) -> tuple:
        """
        Returns an encrypted challenge based on the TEA algortithm

 C++ signature :
  boost::python::tuple encrypt_challenge(int,int [,int=0])
        :param dongle1: dongle1
        :type dongle1: int
        :param dongle2: dongle2
        :type dongle2: int
        :param key_index: key_index
        :type key_index: int
        :rtype: tuple
        """
        pass

    @staticmethod
    def encrypt_challenge2(arg1: int) -> int:
        """
        Returns the UMAC hash for the given challenge.

 C++ signature :
  int encrypt_challenge2(int)
        :param arg1: arg1
        :type arg1: int
        :rtype: int
        """
        pass

    @staticmethod
    def get_application():
        """
        Returns the application instance.

 C++ signature :
  TWeakPtr<TPyHandle<ASongApp>> get_application()
        """
        pass

    @staticmethod
    def get_random_int(arg1: int, arg2: int) -> int:
        """
        Returns a random integer from the given range.

 C++ signature :
  int get_random_int(int,int)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: int
        :rtype: int
        """
        pass

    class Application(object):
        def __init__(self, *a, **k):
            """
            This class represents the Live application.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def average_process_usage(self) -> None:
            """
            Reports Live's average CPU load.
            """
            pass

        @property
        def browser(self) -> None:
            """
            Returns an interface to the browser.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Returns the canonical parent of the application.
            """
            pass

        @property
        def control_surfaces(self) -> None:
            """
            Const access to a list of the control surfaces selected in preferences, in the same order.
The list contains None if no control surface is active at that index.
            """
            pass

        @property
        def current_dialog_button_count(self) -> None:
            """
            Number of buttons on the current dialog.
            """
            pass

        @property
        def current_dialog_message(self) -> None:
            """
            Text of the last dialog that appeared; Empty if all dialogs just disappeared.
            """
            pass

        @property
        def number_of_push_apps_running(self) -> None:
            """
            Returns the number of connected Push apps.
            """
            pass

        @property
        def open_dialog_count(self) -> None:
            """
            The number of open dialogs in Live. 0 if not dialog is open.
            """
            pass

        @property
        def peak_process_usage(self) -> None:
            """
            Reports Live's peak CPU load.
            """
            pass

        @property
        def unavailable_features(self) -> None:
            """
            List of features that are unavailable due to limitations of the current Live edition.
            """
            pass

        @property
        def view(self) -> None:
            """
            Returns the applications view component.
            """
            pass

        def add_average_process_usage_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "average_process_usage" has changed.

 C++ signature :
  void add_average_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_control_surfaces_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "control_surfaces" has changed.

 C++ signature :
  void add_control_surfaces_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_open_dialog_count_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "open_dialog_count" has changed.

 C++ signature :
  void add_open_dialog_count_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_peak_process_usage_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "peak_process_usage" has changed.

 C++ signature :
  void add_peak_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_unavailable_features_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "unavailable_features" has changed.

 C++ signature :
  void add_unavailable_features_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def average_process_usage_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "average_process_usage".

 C++ signature :
  bool average_process_usage_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def control_surfaces_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "control_surfaces".

 C++ signature :
  bool control_surfaces_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def get_bugfix_version(self, ) -> int:
            """
            Returns an integer representing the bugfix version of Live.

 C++ signature :
  int get_bugfix_version(TPyHandle<ASongApp>)
            :rtype: int
            """
            pass

        def get_build_id(self, ) -> str:
            """
            Returns a string identifying the build.

 C++ signature :
  TString get_build_id(TPyHandle<ASongApp>)
            :rtype: str
            """
            pass

        def get_document(self, ) -> Song:
            """
            Returns the current Live Set.

 C++ signature :
  TWeakPtr<TPyHandle<ASong>> get_document(TPyHandle<ASongApp>)
            :rtype: Song
            """
            pass

        def get_major_version(self, ) -> int:
            """
            Returns an integer representing the major version of Live.

 C++ signature :
  int get_major_version(TPyHandle<ASongApp>)
            :rtype: int
            """
            pass

        def get_minor_version(self, ) -> int:
            """
            Returns an integer representing the minor version of Live.

 C++ signature :
  int get_minor_version(TPyHandle<ASongApp>)
            :rtype: int
            """
            pass

        def get_variant(self, ) -> str:
            """
            Returns one of the strings in Live.Application.Variants.

 C++ signature :
  TString get_variant(TPyHandle<ASongApp>)
            :rtype: str
            """
            pass

        def get_version_string(self, ) -> str:
            """
            Returns the full version string of Live.

 C++ signature :
  TString get_version_string(TPyHandle<ASongApp>)
            :rtype: str
            """
            pass

        def has_option(self, arg2: object) -> bool:
            """
            Returns True if the given entry exists in Options.txt, False otherwise.

 C++ signature :
  bool has_option(TPyHandle<ASongApp>,TString)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def open_dialog_count_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "open_dialog_count".

 C++ signature :
  bool open_dialog_count_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def peak_process_usage_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "peak_process_usage".

 C++ signature :
  bool peak_process_usage_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def press_current_dialog_button(self, arg2: int) -> None:
            """
            Press a button, by index, on the current message box.

 C++ signature :
  void press_current_dialog_button(TPyHandle<ASongApp>,int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def remove_average_process_usage_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "average_process_usage".

 C++ signature :
  void remove_average_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_control_surfaces_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "control_surfaces".

 C++ signature :
  void remove_control_surfaces_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_open_dialog_count_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "open_dialog_count".

 C++ signature :
  void remove_open_dialog_count_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_peak_process_usage_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "peak_process_usage".

 C++ signature :
  void remove_peak_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_unavailable_features_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "unavailable_features".

 C++ signature :
  void remove_unavailable_features_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def show_message(self, text: Text, buttons: int, enable_markup: bool, show_success_icon: bool) -> int:
            """
            Shows a message box, returning the position of the pressed button.

 C++ signature :
  int show_message(TPyHandle<ASongApp>,TText [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False]]])
            :param text: text
            :type text: Text
            :param buttons: buttons
            :type buttons: int
            :param enable_markup: enable_markup
            :type enable_markup: bool
            :param show_success_icon: show_success_icon
            :type show_success_icon: bool
            :rtype: int
            """
            pass

        def show_on_the_fly_message(self, message: str, buttons: int, enable_markup: bool, show_success_icon: bool, push_dialog_type: int) -> int:
            """
            Same as show_message, but for when there is no predefined Text object.

 C++ signature :
  int show_on_the_fly_message(TPyHandle<ASongApp>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False [,int=Application.PushDialogType.MESSAGE_BOX]]]])
            :param message: message
            :type message: str
            :param buttons: buttons
            :type buttons: int
            :param enable_markup: enable_markup
            :type enable_markup: bool
            :param show_success_icon: show_success_icon
            :type show_success_icon: bool
            :param push_dialog_type: push_dialog_type
            :type push_dialog_type: int
            :rtype: int
            """
            pass

        def unavailable_features_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "unavailable_features".

 C++ signature :
  bool unavailable_features_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                This class represents the view aspects of the Live application.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def browse_mode(self) -> None:
                """
                Return true if HotSwap mode is active for any target.
                """
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the application view.
                """
                pass

            @property
            def focused_document_view(self) -> None:
                """
                Return the name of the document view ('Session' or 'Arranger')
shown in the currently selected window.
                """
                pass

            def add_browse_mode_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "browse_mode" has changed.

 C++ signature :
  void add_browse_mode_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_focused_document_view_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "focused_document_view" has changed.

 C++ signature :
  void add_focused_document_view_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_is_view_visible_listener(self, arg2: object, arg3: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_view_visible" has changed.

 C++ signature :
  void add_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :param arg3: arg3
                :type arg3: object
                :rtype: None
                """
                pass

            def add_view_focus_changed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "view_focus_changed" has changed.

 C++ signature :
  void add_view_focus_changed_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def available_main_views(self, ) -> StringVector:
                """
                Return a list of strings with the available subcomponent views, which
 is to be specified, when using the rest of this classes functions.
 A 'subcomponent view' is a main view component of a document view, like
 the Session view, the Arranger or Detailview and so on...

 C++ signature :
  std::__1::vector<TString, std::__1::allocator<TString>> available_main_views(TPyViewData<ASongApp>)
                :rtype: StringVector
                """
                pass

            def browse_mode_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "browse_mode".

 C++ signature :
  bool browse_mode_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def focus_view(self, arg2: object) -> None:
                """
                Show and focus one through the identifier string specified view.

 C++ signature :
  void focus_view(TPyViewData<ASongApp>,TString)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def focused_document_view_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "focused_document_view".

 C++ signature :
  bool focused_document_view_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def hide_view(self, arg2: object) -> None:
                """
                Hide one through the identifier string specified view.

 C++ signature :
  void hide_view(TPyViewData<ASongApp>,TString)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_view_visible(self, identifier: object, main_window_only: bool) -> bool:
                """
                Return true if the through the identifier string specified view is currently
 visible. If main_window_only is set to False, this will also check in second
 window. Notifications from the second window are not yet supported.

 C++ signature :
  bool is_view_visible(TPyViewData<ASongApp>,TString [,bool=True])
                :param identifier: identifier
                :type identifier: object
                :param main_window_only: main_window_only
                :type main_window_only: bool
                :rtype: bool
                """
                pass

            def is_view_visible_has_listener(self, arg2: object, arg3: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_view_visible".

 C++ signature :
  bool is_view_visible_has_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :param arg3: arg3
                :type arg3: object
                :rtype: bool
                """
                pass

            def remove_browse_mode_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "browse_mode".

 C++ signature :
  void remove_browse_mode_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_focused_document_view_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "focused_document_view".

 C++ signature :
  void remove_focused_document_view_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_is_view_visible_listener(self, arg2: object, arg3: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_view_visible".

 C++ signature :
  void remove_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :param arg3: arg3
                :type arg3: object
                :rtype: None
                """
                pass

            def remove_view_focus_changed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "view_focus_changed".

 C++ signature :
  void remove_view_focus_changed_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def scroll_view(self, arg2: int, arg3: object, arg4: bool) -> None:
                """
                Scroll through the identifier string specified view into the given
 direction, if possible.  Will silently return if the specified view
 can not perform the requested action.

 C++ signature :
  void scroll_view(TPyViewData<ASongApp>,int,TString,bool)
                :param arg2: arg2
                :type arg2: int
                :param arg3: arg3
                :type arg3: object
                :param arg4: arg4
                :type arg4: bool
                :rtype: None
                """
                pass

            def show_view(self, arg2: object) -> None:
                """
                Show one through the identifier string specified view. Will throw a
 runtime error if this is called in Live's initialization scope.

 C++ signature :
  void show_view(TPyViewData<ASongApp>,TString)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def toggle_browse(self, ) -> None:
                """
                Reveals the device chain, the browser and starts hot swap for
 the selected device. Calling this function again stops hot swap.

 C++ signature :
  void toggle_browse(TPyViewData<ASongApp>)
                :rtype: None
                """
                pass

            def view_focus_changed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "view_focus_changed".

 C++ signature :
  bool view_focus_changed_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def zoom_view(self, arg2: int, arg3: object, arg4: bool) -> None:
                """
                Zoom through the identifier string specified view into the given
 direction, if possible.  Will silently return if the specified view
 can not perform the requested action.

 C++ signature :
  void zoom_view(TPyViewData<ASongApp>,int,TString,bool)
                :param arg2: arg2
                :type arg2: int
                :param arg3: arg3
                :type arg3: object
                :param arg4: arg4
                :type arg4: bool
                :rtype: None
                """
                pass

            class NavDirection(object):
                def __init__(self, *a, **k):
                    pass

                def from_bytes(self, *a, **k) -> None:
                    """
                    Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
                    """
                    pass

    class ControlDescription(object):
        def __init__(self, *a, **k):
            """
            Describes a control present in a control surface proxy
            """
            pass

        @property
        def id(self) -> None:
            pass

        @property
        def name(self) -> None:
            pass

    class ControlDescriptionVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning control descriptions.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<TControlDescription, std::__1::allocator<TControlDescription>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<TControlDescription, std::__1::allocator<TControlDescription>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class ControlSurfaceProxy(object):
        def __init__(self, *a, **k):
            """
            Represents a control surface running in a different process. For use by M4L
            """
            pass

        @property
        def control_descriptions(self) -> None:
            pass

        @property
        def type_name(self) -> None:
            pass

        def add_control_values_arrived_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "control_values_arrived" has changed.

 C++ signature :
  void add_control_values_arrived_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_midi_received_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "midi_received" has changed.

 C++ signature :
  void add_midi_received_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def control_values_arrived_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "control_values_arrived".

 C++ signature :
  bool control_values_arrived_has_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def enable_receive_midi(self, arg2: bool) -> None:
            """
            C++ signature :
  void enable_receive_midi(APythonControlSurfaceProxy {lvalue},bool)
            :param arg2: arg2
            :type arg2: bool
            :rtype: None
            """
            pass

        def fetch_received_midi_messages(self, ) -> tuple:
            """
            C++ signature :
  boost::python::tuple fetch_received_midi_messages(APythonControlSurfaceProxy {lvalue})
            :rtype: tuple
            """
            pass

        def fetch_received_values(self, ) -> tuple:
            """
            C++ signature :
  boost::python::tuple fetch_received_values(APythonControlSurfaceProxy {lvalue})
            :rtype: tuple
            """
            pass

        def grab_control(self, arg2: int) -> None:
            """
            C++ signature :
  void grab_control(APythonControlSurfaceProxy {lvalue},int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def midi_received_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "midi_received".

 C++ signature :
  bool midi_received_has_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def release_control(self, arg2: int) -> None:
            """
            C++ signature :
  void release_control(APythonControlSurfaceProxy {lvalue},int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def remove_control_values_arrived_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "control_values_arrived".

 C++ signature :
  void remove_control_values_arrived_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_midi_received_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "midi_received".

 C++ signature :
  void remove_midi_received_listener(APythonControlSurfaceProxy,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def send_midi(self, arg2: tuple) -> None:
            """
            C++ signature :
  void send_midi(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
            :param arg2: arg2
            :type arg2: tuple
            :rtype: None
            """
            pass

        def send_value(self, arg2: tuple) -> None:
            """
            C++ signature :
  void send_value(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
            :param arg2: arg2
            :type arg2: tuple
            :rtype: None
            """
            pass

        def subscribe_to_control(self, arg2: int) -> None:
            """
            C++ signature :
  void subscribe_to_control(APythonControlSurfaceProxy {lvalue},int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def unsubscribe_from_control(self, arg2: int) -> None:
            """
            C++ signature :
  void unsubscribe_from_control(APythonControlSurfaceProxy {lvalue},int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

    class MessageButtons(object):
        def __init__(self, *a, **k):
            """
            Specifies the characteristics of the message box, e.g. which buttons to show.
            """
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class PushDialogType(object):
        def __init__(self, *a, **k):
            """
            Specifies the dialog type for Push.
            """
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class UnavailableFeature(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class UnavailableFeatureVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning unavailable features.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<NPythonApplication::TUnavailableFeature, std::__1::allocator<NPythonApplication::TUnavailableFeature>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<NPythonApplication::TUnavailableFeature, std::__1::allocator<NPythonApplication::TUnavailableFeature>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class Variants(object):
        def __init__(self, *a, **k):
            """
            Holds strings representing what type of Live is running.
            """
            pass


class Base(ModuleType):
    pass

    @staticmethod
    def get_text(classname: str, textname: str) -> Text:
        """
        Retrieves the (translated) Text identified by `classname` and `textname`.

 C++ signature :
  TText const* get_text(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
        :param classname: classname
        :type classname: str
        :param textname: textname
        :type textname: str
        :rtype: Text
        """
        pass

    @staticmethod
    def log(arg1: str) -> None:
        """
        C++ signature :
  void log(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
        :param arg1: arg1
        :type arg1: str
        :rtype: None
        """
        pass

    @staticmethod
    def subst_args(text: Text, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str) -> str:
        """
        C++ signature :
  std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> subst_args(TText [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='']]]]])
        :param text: text
        :type text: Text
        :param arg1: arg1
        :type arg1: str
        :param arg2: arg2
        :type arg2: str
        :param arg3: arg3
        :type arg3: str
        :param arg4: arg4
        :type arg4: str
        :param arg5: arg5
        :type arg5: str
        :rtype: str
        """
        pass

    class FloatVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning floats from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<float, std::__1::allocator<float>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<float, std::__1::allocator<float>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class IntU64Vector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning unsigned long integers from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class IntVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning integers from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<int, std::__1::allocator<int>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<int, std::__1::allocator<int>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class LimitationError(object):
        def __init__(self, *a, **k):
            pass

    class ObjectVector(object):
        def __init__(self, *a, **k):
            """
            A simple read only container for returning python objects.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class StringVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning strings from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<TString, std::__1::allocator<TString>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<TString, std::__1::allocator<TString>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class Text(object):
        def __init__(self, *a, **k):
            """
            A translatable, immutable string.
            """
            pass

        @property
        def text(self) -> None:
            pass

    class Timer(object):
        def __init__(self, *a, **k):
            """
            A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer.
            """
            pass

        @property
        def running(self) -> None:
            pass

        def restart(self, ) -> None:
            """
            C++ signature :
  void restart(PythonTimer {lvalue})
            :rtype: None
            """
            pass

        def start(self, ) -> None:
            """
            C++ signature :
  void start(PythonTimer {lvalue})
            :rtype: None
            """
            pass

        def stop(self, ) -> None:
            """
            C++ signature :
  void stop(PythonTimer {lvalue})
            :rtype: None
            """
            pass

    class Vector(object):
        def __init__(self, *a, **k):
            """
            A simple read only container for returning objects from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<TWeakPtr<TPyHandleBase>, std::__1::allocator<TWeakPtr<TPyHandleBase>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<TWeakPtr<TPyHandleBase>, std::__1::allocator<TWeakPtr<TPyHandleBase>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass


class Browser(ModuleType):
    pass

    class Browser(object):
        def __init__(self, *a, **k):
            """
            This class represents the live browser data base.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def audio_effects(self) -> None:
            """
            Returns a browser item with access to all the Audio Effects content.
            """
            pass

        @property
        def clips(self) -> None:
            """
            Returns a browser item with access to all the Clips content.
            """
            pass

        @property
        def colors(self) -> None:
            """
            Returns a list of browser items containing the configured colors.
            """
            pass

        @property
        def current_project(self) -> None:
            """
            Returns a browser item with access to all the Current Project content.
            """
            pass

        @property
        def drums(self) -> None:
            """
            Returns a browser item with access to all the Drums content.
            """
            pass

        @property
        def filter_type(self) -> None:
            """
            Bang triggered when the hotswap target has changed.
            """
            pass

        @property
        def hotswap_target(self) -> None:
            """
            Bang triggered when the hotswap target has changed.
            """
            pass

        @property
        def instruments(self) -> None:
            """
            Returns a browser item with access to all the Instruments content.
            """
            pass

        @property
        def legacy_libraries(self) -> None:
            """
            Returns a list of browser items containing the installed legacy libraries. The list is always empty as legacy library handling has been removed.
            """
            pass

        @property
        def max_for_live(self) -> None:
            """
            Returns a browser item with access to all the Max For Live content.
            """
            pass

        @property
        def midi_effects(self) -> None:
            """
            Returns a browser item with access to all the Midi Effects content.
            """
            pass

        @property
        def packs(self) -> None:
            """
            Returns a browser item with access to all the Packs content.
            """
            pass

        @property
        def plugins(self) -> None:
            """
            Returns a browser item with access to all the Plugins content.
            """
            pass

        @property
        def samples(self) -> None:
            """
            Returns a browser item with access to all the Samples content.
            """
            pass

        @property
        def sounds(self) -> None:
            """
            Returns a browser item with access to all the Sounds content.
            """
            pass

        @property
        def user_folders(self) -> None:
            """
            Returns a list of browser items containing all the user folders.
            """
            pass

        @property
        def user_library(self) -> None:
            """
            Returns a browser item with access to all the User Library content.
            """
            pass

        def add_filter_type_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "filter_type" has changed.

 C++ signature :
  void add_filter_type_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_full_refresh_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "full_refresh" has changed.

 C++ signature :
  void add_full_refresh_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_hotswap_target_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "hotswap_target" has changed.

 C++ signature :
  void add_hotswap_target_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def filter_type_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "filter_type".

 C++ signature :
  bool filter_type_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def full_refresh_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "full_refresh".

 C++ signature :
  bool full_refresh_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def hotswap_target_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "hotswap_target".

 C++ signature :
  bool hotswap_target_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def load_item(self, arg2: BrowserItem) -> None:
            """
            Loads the provided browser item.

 C++ signature :
  void load_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
            :param arg2: arg2
            :type arg2: BrowserItem
            :rtype: None
            """
            pass

        def preview_item(self, arg2: BrowserItem) -> None:
            """
            Previews the provided browser item.

 C++ signature :
  void preview_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
            :param arg2: arg2
            :type arg2: BrowserItem
            :rtype: None
            """
            pass

        def relation_to_hotswap_target(self, arg2: BrowserItem) -> Relation:
            """
            Returns the relation between the given browser item and the current hotswap target

 C++ signature :
  ableton::live_library::Relation relation_to_hotswap_target(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
            :param arg2: arg2
            :type arg2: BrowserItem
            :rtype: Relation
            """
            pass

        def remove_filter_type_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "filter_type".

 C++ signature :
  void remove_filter_type_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_full_refresh_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "full_refresh".

 C++ signature :
  void remove_full_refresh_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_hotswap_target_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "hotswap_target".

 C++ signature :
  void remove_hotswap_target_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def stop_preview(self, ) -> None:
            """
            Stop the current preview.

 C++ signature :
  void stop_preview(TPyHandle<ABrowserDelegate>)
            :rtype: None
            """
            pass

    class BrowserItem(object):
        def __init__(self, *a, **k):
            """
            This class represents an item of the browser hierarchy.
            """
            pass

        @property
        def children(self) -> None:
            """
            Const access to the descendants of this browser item.
            """
            pass

        @property
        def is_device(self) -> None:
            """
            Indicates if the browser item represents a device.
            """
            pass

        @property
        def is_folder(self) -> None:
            """
            Indicates if the browser item represents folder.
            """
            pass

        @property
        def is_loadable(self) -> None:
            """
            True if item can be loaded via the Browser's 'load_item' method.
            """
            pass

        @property
        def is_selected(self) -> None:
            """
            True if the item is ancestor of or the actual selection.
            """
            pass

        @property
        def iter_children(self) -> None:
            """
            Const iterable access to the descendants of this browser item.
            """
            pass

        @property
        def name(self) -> None:
            """
            Const access to the canonical display name of this browser item.
            """
            pass

        @property
        def source(self) -> None:
            """
            Specifies where does item come from -- i.e. Live pack, user library...
            """
            pass

        @property
        def uri(self) -> None:
            """
            The uri describes a unique identifier for a browser item.
            """
            pass

    class BrowserItemIterator(object):
        def __init__(self, *a, **k):
            """
            This class iterates over children of another BrowserItem.
            """
            pass

    class BrowserItemVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning browser items from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<NPythonBrowser::TPythonBrowserItem, std::__1::allocator<NPythonBrowser::TPythonBrowserItem>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<NPythonBrowser::TPythonBrowserItem, std::__1::allocator<NPythonBrowser::TPythonBrowserItem>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class FilterType(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class Relation(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class CcControlDevice(ModuleType):
    pass

    class CcControlDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a CcControl device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def custom_bool_target(self) -> None:
            """
            Return the custom bool target
            """
            pass

        @property
        def custom_bool_target_list(self) -> None:
            """
            Return the custom bool target list
            """
            pass

        @property
        def custom_float_target_0(self) -> None:
            """
            Return the custom float target 0
            """
            pass

        @property
        def custom_float_target_0_list(self) -> None:
            """
            Return the custom float target 0 list
            """
            pass

        @property
        def custom_float_target_1(self) -> None:
            """
            Return the custom float target 1
            """
            pass

        @property
        def custom_float_target_10(self) -> None:
            """
            Return the custom float target 10
            """
            pass

        @property
        def custom_float_target_10_list(self) -> None:
            """
            Return the custom float target 10 list
            """
            pass

        @property
        def custom_float_target_11(self) -> None:
            """
            Return the custom float target 11
            """
            pass

        @property
        def custom_float_target_11_list(self) -> None:
            """
            Return the custom float target 11 list
            """
            pass

        @property
        def custom_float_target_1_list(self) -> None:
            """
            Return the custom float target 1 list
            """
            pass

        @property
        def custom_float_target_2(self) -> None:
            """
            Return the custom float target 2
            """
            pass

        @property
        def custom_float_target_2_list(self) -> None:
            """
            Return the custom float target 2 list
            """
            pass

        @property
        def custom_float_target_3(self) -> None:
            """
            Return the custom float target 3
            """
            pass

        @property
        def custom_float_target_3_list(self) -> None:
            """
            Return the custom float target 3 list
            """
            pass

        @property
        def custom_float_target_4(self) -> None:
            """
            Return the custom float target 4
            """
            pass

        @property
        def custom_float_target_4_list(self) -> None:
            """
            Return the custom float target 4 list
            """
            pass

        @property
        def custom_float_target_5(self) -> None:
            """
            Return the custom float target 5
            """
            pass

        @property
        def custom_float_target_5_list(self) -> None:
            """
            Return the custom float target 5 list
            """
            pass

        @property
        def custom_float_target_6(self) -> None:
            """
            Return the custom float target 6
            """
            pass

        @property
        def custom_float_target_6_list(self) -> None:
            """
            Return the custom float target 6 list
            """
            pass

        @property
        def custom_float_target_7(self) -> None:
            """
            Return the custom float target 7
            """
            pass

        @property
        def custom_float_target_7_list(self) -> None:
            """
            Return the custom float target 7 list
            """
            pass

        @property
        def custom_float_target_8(self) -> None:
            """
            Return the custom float target 8
            """
            pass

        @property
        def custom_float_target_8_list(self) -> None:
            """
            Return the custom float target 8 list
            """
            pass

        @property
        def custom_float_target_9(self) -> None:
            """
            Return the custom float target 9
            """
            pass

        @property
        def custom_float_target_9_list(self) -> None:
            """
            Return the custom float target 9 list
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_custom_bool_target_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_bool_target" has changed.

 C++ signature :
  void add_custom_bool_target_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_0_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_0" has changed.

 C++ signature :
  void add_custom_float_target_0_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_10_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_10" has changed.

 C++ signature :
  void add_custom_float_target_10_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_11_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_11" has changed.

 C++ signature :
  void add_custom_float_target_11_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_1_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_1" has changed.

 C++ signature :
  void add_custom_float_target_1_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_2_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_2" has changed.

 C++ signature :
  void add_custom_float_target_2_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_3_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_3" has changed.

 C++ signature :
  void add_custom_float_target_3_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_4_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_4" has changed.

 C++ signature :
  void add_custom_float_target_4_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_5_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_5" has changed.

 C++ signature :
  void add_custom_float_target_5_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_6_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_6" has changed.

 C++ signature :
  void add_custom_float_target_6_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_7_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_7" has changed.

 C++ signature :
  void add_custom_float_target_7_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_8_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_8" has changed.

 C++ signature :
  void add_custom_float_target_8_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_custom_float_target_9_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "custom_float_target_9" has changed.

 C++ signature :
  void add_custom_float_target_9_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def custom_bool_target_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_bool_target".

 C++ signature :
  bool custom_bool_target_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_0_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_0".

 C++ signature :
  bool custom_float_target_0_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_10_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_10".

 C++ signature :
  bool custom_float_target_10_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_11_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_11".

 C++ signature :
  bool custom_float_target_11_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_1_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_1".

 C++ signature :
  bool custom_float_target_1_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_2_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_2".

 C++ signature :
  bool custom_float_target_2_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_3_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_3".

 C++ signature :
  bool custom_float_target_3_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_4_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_4".

 C++ signature :
  bool custom_float_target_4_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_5_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_5".

 C++ signature :
  bool custom_float_target_5_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_6_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_6".

 C++ signature :
  bool custom_float_target_6_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_7_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_7".

 C++ signature :
  bool custom_float_target_7_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_8_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_8".

 C++ signature :
  bool custom_float_target_8_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def custom_float_target_9_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "custom_float_target_9".

 C++ signature :
  bool custom_float_target_9_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_custom_bool_target_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_bool_target".

 C++ signature :
  void remove_custom_bool_target_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_0_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_0".

 C++ signature :
  void remove_custom_float_target_0_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_10_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_10".

 C++ signature :
  void remove_custom_float_target_10_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_11_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_11".

 C++ signature :
  void remove_custom_float_target_11_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_1_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_1".

 C++ signature :
  void remove_custom_float_target_1_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_2_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_2".

 C++ signature :
  void remove_custom_float_target_2_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_3_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_3".

 C++ signature :
  void remove_custom_float_target_3_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_4_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_4".

 C++ signature :
  void remove_custom_float_target_4_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_5_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_5".

 C++ signature :
  void remove_custom_float_target_5_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_6_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_6".

 C++ signature :
  void remove_custom_float_target_6_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_7_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_7".

 C++ signature :
  void remove_custom_float_target_7_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_8_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_8".

 C++ signature :
  void remove_custom_float_target_8_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_custom_float_target_9_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "custom_float_target_9".

 C++ signature :
  void remove_custom_float_target_9_listener(TCcControlDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def resend(self, ) -> None:
            """
            Resend all CC values.

 C++ signature :
  void resend(TCcControlDevicePyHandle)
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class Chain(ModuleType):
    pass

    class Chain(object):
        def __init__(self, *a, **k):
            """
            This class represents a group device chain in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the chain.
            """
            pass

        @property
        def color(self) -> None:
            """
            Access the color index of the Chain.
            """
            pass

        @property
        def color_index(self) -> None:
            """
            Access the color index of the Chain.
            """
            pass

        @property
        def devices(self) -> None:
            """
            Return const access to all available Devices that are present in the chains
            """
            pass

        @property
        def has_audio_input(self) -> None:
            """
            return True, if this Chain can be feed with an Audio signal. This is
true for all Audio Chains.
            """
            pass

        @property
        def has_audio_output(self) -> None:
            """
            return True, if this Chain sends out an Audio signal. This is
true for all Audio Chains, and MIDI chains with an Instrument.
            """
            pass

        @property
        def has_midi_input(self) -> None:
            """
            return True, if this Chain can be feed with an Audio signal. This is
true for all MIDI Chains.
            """
            pass

        @property
        def has_midi_output(self) -> None:
            """
            return True, if this Chain sends out MIDI events. This is
true for all MIDI Chains with no Instruments.
            """
            pass

        @property
        def is_auto_colored(self) -> None:
            """
            Get/set access to the auto color flag of the Chain.
If True, the Chain will always have the same color as the containing
Track or Chain.
            """
            pass

        @property
        def mixer_device(self) -> Return access to the mixer device that holds the chain's mixer parameters:
            """
            the Volume, Pan, and Sendamounts.
            """
            pass

        @property
        def mute(self) -> None:
            """
            Mute/unmute the chain.
            """
            pass

        @property
        def muted_via_solo(self) -> None:
            """
            Return const access to whether this chain is muted due to some other chain
being soloed.
            """
            pass

        @property
        def name(self) -> None:
            """
            Read/write access to the name of the Chain, as visible in the track header.
            """
            pass

        @property
        def solo(self) -> None:
            """
            Get/Set the solo status of the chain. Note that this will not disable the
solo state of any other Chain in the same rack. If you want exclusive solo, 
you have to disable the solo state of the other Chains manually.
            """
            pass

        def add_color_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color_index" has changed.

 C++ signature :
  void add_color_index_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color" has changed.

 C++ signature :
  void add_color_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_devices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "devices" has changed.

 C++ signature :
  void add_devices_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_auto_colored_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_auto_colored" has changed.

 C++ signature :
  void add_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mute_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mute" has changed.

 C++ signature :
  void add_mute_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_muted_via_solo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "muted_via_solo" has changed.

 C++ signature :
  void add_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_solo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "solo" has changed.

 C++ signature :
  void add_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def color_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color".

 C++ signature :
  bool color_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color_index".

 C++ signature :
  bool color_index_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def delete_device(self, arg2: int) -> None:
            """
            Remove a device identified by its index from the chain. Throws runtime error if bad index.
 

 C++ signature :
  void delete_device(TChainPyHandle,int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def devices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "devices".

 C++ signature :
  bool devices_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_auto_colored_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_auto_colored".

 C++ signature :
  bool is_auto_colored_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mute_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mute".

 C++ signature :
  bool mute_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def muted_via_solo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "muted_via_solo".

 C++ signature :
  bool muted_via_solo_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_color_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color_index".

 C++ signature :
  void remove_color_index_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color".

 C++ signature :
  void remove_color_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_devices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "devices".

 C++ signature :
  void remove_devices_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_auto_colored_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_auto_colored".

 C++ signature :
  void remove_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mute_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mute".

 C++ signature :
  void remove_mute_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_muted_via_solo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "muted_via_solo".

 C++ signature :
  void remove_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_solo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "solo".

 C++ signature :
  void remove_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def solo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "solo".

 C++ signature :
  bool solo_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class ChainMixerDevice(ModuleType):
    pass

    class ChainMixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Chain's Mixer Device in Live, which gives you
access to the Volume, Panning, and Send properties of a Chain.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the mixer device.
            """
            pass

        @property
        def chain_activator(self) -> None:
            """
            Const access to the Chain's Activator Device Parameter.
            """
            pass

        @property
        def panning(self) -> None:
            """
            Const access to the Chain's Panning Device Parameter.
            """
            pass

        @property
        def sends(self) -> None:
            """
            Const access to the Chain's list of Send Amount Device Parameters.
            """
            pass

        @property
        def volume(self) -> None:
            """
            Const access to the Chain's Volume Device Parameter.
            """
            pass

        def add_sends_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "sends" has changed.

 C++ signature :
  void add_sends_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_sends_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "sends".

 C++ signature :
  void remove_sends_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def sends_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "sends".

 C++ signature :
  bool sends_has_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class Clip(ModuleType):
    pass

    class AutomationEnvelope(object):
        def __init__(self, *a, **k):
            """
            Describes parameter automation per clip.
            """
            pass

        def insert_step(self, arg2: float, arg3: float, arg4: float) -> None:
            """
            C++ signature :
  void insert_step(AAutomation {lvalue},double,double,double)
            :param arg2: arg2
            :type arg2: float
            :param arg3: arg3
            :type arg3: float
            :param arg4: arg4
            :type arg4: float
            :rtype: None
            """
            pass

        def value_at_time(self, arg2: float) -> float:
            """
            C++ signature :
  double value_at_time(AAutomation {lvalue},double)
            :param arg2: arg2
            :type arg2: float
            :rtype: float
            """
            pass

    class Clip(object):
        def __init__(self, *a, **k):
            """
            This class represents a Clip in Live. It can be either an Audio
Clip or a MIDI Clip, in an Arrangement or the Session, depending
on the Track (Slot) it lives in.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def available_warp_modes(self) -> None:
            """
            Available for AudioClips only.
Get/Set the available warp modes, that can be used.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Clip.
            """
            pass

        @property
        def color(self) -> None:
            """
            Get/set access to the color of the Clip (RGB).
            """
            pass

        @property
        def color_index(self) -> None:
            """
            Get/set access to the color index of the Clip.
            """
            pass

        @property
        def end_marker(self) -> None:
            """
            Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def end_time(self) -> None:
            """
            Get the clip's end time.
            """
            pass

        @property
        def file_path(self) -> None:
            """
            Get the path of the file represented by the Audio Clip.
            """
            pass

        @property
        def gain(self) -> None:
            """
            Available for AudioClips only.
Read/write access to the gain setting of the
Audio Clip
            """
            pass

        @property
        def gain_display_string(self) -> None:
            """
            Return a string with the gain as dB value
            """
            pass

        @property
        def groove(self) -> None:
            """
            Get the groove associated with this clip.
            """
            pass

        @property
        def has_envelopes(self) -> None:
            """
            Will notify if the clip gets his first envelope or the last envelope is removed.
            """
            pass

        @property
        def has_groove(self) -> None:
            """
            Returns true if a groove is associated with this clip.
            """
            pass

        @property
        def is_arrangement_clip(self) -> None:
            """
            return true if this Clip is an Arrangement Clip.
A Clip can be either a Session or Arrangement Clip.
            """
            pass

        @property
        def is_audio_clip(self) -> None:
            """
            Return true if this Clip is an Audio Clip.
A Clip can be either an Audioclip or a MIDI Clip.
            """
            pass

        @property
        def is_midi_clip(self) -> None:
            """
            return true if this Clip is a MIDI Clip.
A Clip can be either an Audioclip or a MIDI Clip.
            """
            pass

        @property
        def is_overdubbing(self) -> None:
            """
            returns true if the Clip is recording overdubs
            """
            pass

        @property
        def is_playing(self) -> None:
            """
            Get/Set if this Clip is currently playing. If the Clips trigger mode
is set to a quantization value, the Clip will not start playing immediately.
If you need to know wether the Clip was triggered, use the is_triggered property.
            """
            pass

        @property
        def is_recording(self) -> None:
            """
            returns true if the Clip was triggered to record or is recording.
            """
            pass

        @property
        def is_triggered(self) -> None:
            """
            returns true if the Clip was triggered or is playing.
            """
            pass

        @property
        def launch_mode(self) -> None:
            """
            Get/Set access to the launch mode setting of the Clip.
            """
            pass

        @property
        def launch_quantization(self) -> None:
            """
            Get/Set access to the launch quantization setting of the Clip.
            """
            pass

        @property
        def legato(self) -> None:
            """
            Get/Set access to the legato setting of the Clip
            """
            pass

        @property
        def length(self) -> None:
            """
            Get to the Clips length in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def loop_end(self) -> None:
            """
            Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def loop_start(self) -> None:
            """
            Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def looping(self) -> None:
            """
            Get/Set the Clips 'loop is enabled' flag
.Only Warped Audio Clips or MIDI Clip can be looped.
            """
            pass

        @property
        def muted(self) -> None:
            """
            Read/write access to the mute state of the Clip.
            """
            pass

        @property
        def name(self) -> None:
            """
            Read/write access to the name of the Clip.
            """
            pass

        @property
        def pitch_coarse(self) -> None:
            """
            Available for AudioClips only.
Read/write access to the pitch (in halftones) setting of the
Audio Clip, ranging from -48 to 48
            """
            pass

        @property
        def pitch_fine(self) -> None:
            """
            Available for AudioClips only.
Read/write access to the pitch fine setting of the
Audio Clip, ranging from -500 to 500
            """
            pass

        @property
        def playing_position(self) -> None:
            """
            Constant access to the current playing position of the clip.
The returned value is the position in beats for midi and warped audio clips,
or in seconds for unwarped audio clips. Stopped clips will return 0.
            """
            pass

        @property
        def position(self) -> None:
            """
            Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def ram_mode(self) -> None:
            """
            Available for AudioClips only.
Read/write access to the Ram mode setting of the Audio Clip
            """
            pass

        @property
        def sample_length(self) -> None:
            """
            Available for AudioClips only.
Get the sample length in sample time or -1 if there is no sample available.
            """
            pass

        @property
        def sample_rate(self) -> None:
            """
            Available for AudioClips only.
Read-only access to the Clip's sampling rate.
            """
            pass

        @property
        def signature_denominator(self) -> None:
            """
            Get/Set access to the global signature denominator of the Clip.
            """
            pass

        @property
        def signature_numerator(self) -> None:
            """
            Get/Set access to the global signature numerator of the Clip.
            """
            pass

        @property
        def start_marker(self) -> None:
            """
            Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).
            """
            pass

        @property
        def start_time(self) -> None:
            """
            Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement View clips, this is the offset within the arrangement.
            """
            pass

        @property
        def velocity_amount(self) -> None:
            """
            Get/Set access to the velocity to volume amount of the Clip.
            """
            pass

        @property
        def view(self) -> None:
            """
            Get the view of the Clip.
            """
            pass

        @property
        def warp_markers(self) -> None:
            """
            Available for AudioClips only.
Get the warp markers for this audio clip.
            """
            pass

        @property
        def warp_mode(self) -> None:
            """
            Available for AudioClips only.
Get/Set the warp mode for this audio clip.
            """
            pass

        @property
        def warping(self) -> None:
            """
            Available for AudioClips only.
Get/Set if this Clip is timestreched.
            """
            pass

        @property
        def will_record_on_start(self) -> None:
            """
            returns true if the Clip will record on being started.
            """
            pass

        def add_color_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color_index" has changed.

 C++ signature :
  void add_color_index_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color" has changed.

 C++ signature :
  void add_color_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_end_marker_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "end_marker" has changed.

 C++ signature :
  void add_end_marker_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_end_time_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "end_time" has changed.

 C++ signature :
  void add_end_time_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_file_path_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "file_path" has changed.

 C++ signature :
  void add_file_path_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_gain_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "gain" has changed.

 C++ signature :
  void add_gain_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_groove_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "groove" has changed.

 C++ signature :
  void add_groove_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_has_envelopes_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "has_envelopes" has changed.

 C++ signature :
  void add_has_envelopes_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_overdubbing_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_overdubbing" has changed.

 C++ signature :
  void add_is_overdubbing_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_recording_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_recording" has changed.

 C++ signature :
  void add_is_recording_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_launch_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "launch_mode" has changed.

 C++ signature :
  void add_launch_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_launch_quantization_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "launch_quantization" has changed.

 C++ signature :
  void add_launch_quantization_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_legato_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "legato" has changed.

 C++ signature :
  void add_legato_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_loop_end_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "loop_end" has changed.

 C++ signature :
  void add_loop_end_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_loop_jump_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "loop_jump" has changed.

 C++ signature :
  void add_loop_jump_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_loop_start_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "loop_start" has changed.

 C++ signature :
  void add_loop_start_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_looping_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "looping" has changed.

 C++ signature :
  void add_looping_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_muted_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "muted" has changed.

 C++ signature :
  void add_muted_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_new_notes(self, arg2: object) -> IntU64Vector:
            """
            Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification
 objects. The objects will be used to construct new notes in the clip.

 C++ signature :
  std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: IntU64Vector
            """
            pass

        def add_notes_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "notes" has changed.

 C++ signature :
  void add_notes_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_coarse_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_coarse" has changed.

 C++ signature :
  void add_pitch_coarse_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_fine_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_fine" has changed.

 C++ signature :
  void add_pitch_fine_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playing_position_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playing_position" has changed.

 C++ signature :
  void add_playing_position_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playing_status_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playing_status" has changed.

 C++ signature :
  void add_playing_status_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_position_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "position" has changed.

 C++ signature :
  void add_position_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ram_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ram_mode" has changed.

 C++ signature :
  void add_ram_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_signature_denominator_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "signature_denominator" has changed.

 C++ signature :
  void add_signature_denominator_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_signature_numerator_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "signature_numerator" has changed.

 C++ signature :
  void add_signature_numerator_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_start_marker_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "start_marker" has changed.

 C++ signature :
  void add_start_marker_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_velocity_amount_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "velocity_amount" has changed.

 C++ signature :
  void add_velocity_amount_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warp_marker(self, warp_marker: object) -> None:
            """
            Available for AudioClips only.
 Adds the specified warp marker, if possible.

 C++ signature :
  void add_warp_marker(TPyHandle<AClip>,boost::python::api::object)
            :param warp_marker: warp_marker
            :type warp_marker: object
            :rtype: None
            """
            pass

        def add_warp_markers_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warp_markers" has changed.

 C++ signature :
  void add_warp_markers_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warp_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warp_mode" has changed.

 C++ signature :
  void add_warp_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warping_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warping" has changed.

 C++ signature :
  void add_warping_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def apply_note_modifications(self, arg2: MidiNoteVector) -> None:
            """
            Expects a list of notes as returned from get_notes_extended. The content
 of the list will be used to modify existing notes in the clip, based on
 matching note IDs.
 This function should be used when modifying existing notes, e.g. changing the
 velocity or start time. The function ensures that per-note events attached to
 the modified notes are preserved. This is NOT the case when replacing notes
 via a combination of remove_notes_extended and add_new_notes.
 The given list can be a subset of the notes in the clip, but it must not
 contain any notes that are not present in the clip.
 

 C++ signature :
  void apply_note_modifications(TPyHandle<AClip>,std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>>)
            :param arg2: arg2
            :type arg2: MidiNoteVector
            :rtype: None
            """
            pass

        def automation_envelope(self, arg2: DeviceParameter) -> AutomationEnvelope:
            """
            Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.

 C++ signature :
  TWeakPtr<AAutomation> automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
            :param arg2: arg2
            :type arg2: DeviceParameter
            :rtype: AutomationEnvelope
            """
            pass

        def beat_to_sample_time(self, beat_time: float) -> float:
            """
            Available for AudioClips only.
 Converts the given beat time to sample time. Raises an error if the sample is not warped.

 C++ signature :
  double beat_to_sample_time(TPyHandle<AClip>,double)
            :param beat_time: beat_time
            :type beat_time: float
            :rtype: float
            """
            pass

        def clear_all_envelopes(self, ) -> None:
            """
            Clears all envelopes for this clip.

 C++ signature :
  void clear_all_envelopes(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def clear_envelope(self, arg2: DeviceParameter) -> None:
            """
            Clears the envelope of this clips given parameter.

 C++ signature :
  void clear_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
            :param arg2: arg2
            :type arg2: DeviceParameter
            :rtype: None
            """
            pass

        def color_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color".

 C++ signature :
  bool color_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color_index".

 C++ signature :
  bool color_index_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def create_automation_envelope(self, arg2: DeviceParameter) -> AutomationEnvelope:
            """
            Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.

 C++ signature :
  TWeakPtr<AAutomation> create_automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
            :param arg2: arg2
            :type arg2: DeviceParameter
            :rtype: AutomationEnvelope
            """
            pass

        def crop(self, ) -> None:
            """
            Crops the clip. The region that is cropped depends on whether the clip is
 looped or not. If looped, the region outside of the loop is removed.
 If not looped, the region outside the start and end markers is removed.

 C++ signature :
  void crop(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def deselect_all_notes(self, ) -> None:
            """
            De-selects all notes present in the clip.

 C++ signature :
  void deselect_all_notes(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def duplicate_loop(self, ) -> None:
            """
            Make the loop two times longer and duplicates notes and envelopes.
 Duplicates the clip start/end range if the clip is not looped.

 C++ signature :
  void duplicate_loop(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def duplicate_notes_by_id(self, note_ids: object, destination_time: object, transposition_amount: int) -> IntU64Vector:
            """
            Duplicate all notes matching the given note IDs.
 If the optional destination_time is not provided, new notes will be inserted
 after the last selected note. This behavior can be observed when duplicating
 notes in the Live GUI.
 If the transposition_amount is specified, the notes in the region will be
 transposed by the number of semitones.
 Raises an error on audio clips.

 C++ signature :
  std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object [,boost::python::api::object=None [,int=0]])
            :param note_ids: note_ids
            :type note_ids: object
            :param destination_time: destination_time
            :type destination_time: object
            :param transposition_amount: transposition_amount
            :type transposition_amount: int
            :rtype: IntU64Vector
            """
            pass

        def duplicate_region(self, region_start: float, region_length: float, destination_time: float, pitch: int, transposition_amount: int) -> None:
            """
            Duplicate the notes in the specified region to the destination_time.
 Only notes of the specified pitch are duplicated or all if pitch is -1.
 If the transposition_amount is not 0, the notes in the region will
 be transposed by the transpose_amount of semitones.Raises an error on audio clips.

 C++ signature :
  void duplicate_region(TPyHandle<AClip>,double,double,double [,int=-1 [,int=0]])
            :param region_start: region_start
            :type region_start: float
            :param region_length: region_length
            :type region_length: float
            :param destination_time: destination_time
            :type destination_time: float
            :param pitch: pitch
            :type pitch: int
            :param transposition_amount: transposition_amount
            :type transposition_amount: int
            :rtype: None
            """
            pass

        def end_marker_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "end_marker".

 C++ signature :
  bool end_marker_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def end_time_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "end_time".

 C++ signature :
  bool end_time_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def file_path_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "file_path".

 C++ signature :
  bool file_path_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def fire(self, ) -> None:
            """
            (Re)Start playing this Clip.

 C++ signature :
  void fire(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def gain_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "gain".

 C++ signature :
  bool gain_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def get_all_notes_extended(self, ) -> MidiNoteVector:
            """
            Returns a list of all MIDI notes from the clip, regardless of their position
 relative to the start and end markers/loop start and loop end.
 Each note is represented by a Live.Clip.MidiNote object.
 The returned list can be modified freely, but modifications will not
 be reflected in the MIDI clip until apply_note_modifications is called.

 C++ signature :
  std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_all_notes_extended(TPyHandle<AClip>)
            :rtype: MidiNoteVector
            """
            pass

        def get_notes(self, from_time: float, from_pitch: int, time_span: float, pitch_span: int) -> tuple:
            """
            Returns a tuple of tuples where each inner tuple represents
 a note starting in the given pitch- and time range.
 The inner tuple contains pitch, time, duration, velocity, and mute state.

 C++ signature :
  boost::python::tuple get_notes(TPyHandle<AClip>,double,int,double,int)
            :param from_time: from_time
            :type from_time: float
            :param from_pitch: from_pitch
            :type from_pitch: int
            :param time_span: time_span
            :type time_span: float
            :param pitch_span: pitch_span
            :type pitch_span: int
            :rtype: tuple
            """
            pass

        def get_notes_by_id(self, note_ids: object) -> MidiNoteVector:
            """
            Return a list of MIDI notes matching the given note IDs.
 

 C++ signature :
  std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
            :param note_ids: note_ids
            :type note_ids: object
            :rtype: MidiNoteVector
            """
            pass

        def get_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> MidiNoteVector:
            """
            Returns a list of MIDI notes from the given pitch and time range.
 Each note is represented by a Live.Clip.MidiNote object.
 The returned list can be modified freely, but modifications will not
 be reflected in the MIDI clip until apply_note_modifications is called.

 C++ signature :
  std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_extended(TPyHandle<AClip>,int,int,double,double)
            :param from_pitch: from_pitch
            :type from_pitch: int
            :param pitch_span: pitch_span
            :type pitch_span: int
            :param from_time: from_time
            :type from_time: float
            :param time_span: time_span
            :type time_span: float
            :rtype: MidiNoteVector
            """
            pass

        def get_selected_notes(self, ) -> tuple:
            """
            Returns a tuple of tuples where each inner tuple
 represents a selected note. The inner tuple contains
 pitch, time, duration, velocity, and mute state.

 C++ signature :
  boost::python::tuple get_selected_notes(TPyHandle<AClip>)
            :rtype: tuple
            """
            pass

        def get_selected_notes_extended(self, ) -> MidiNoteVector:
            """
            Returns a list of all MIDI notes from the clip that are currently selected.
 Each note is represented by a Live.Clip.MidiNote object.
 The returned list can be modified freely, but modifications will not
 be reflected in the MIDI clip until apply_note_modifications is called.

 C++ signature :
  std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_selected_notes_extended(TPyHandle<AClip>)
            :rtype: MidiNoteVector
            """
            pass

        def groove_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "groove".

 C++ signature :
  bool groove_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def has_envelopes_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "has_envelopes".

 C++ signature :
  bool has_envelopes_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_overdubbing_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_overdubbing".

 C++ signature :
  bool is_overdubbing_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_recording_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_recording".

 C++ signature :
  bool is_recording_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def launch_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "launch_mode".

 C++ signature :
  bool launch_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def launch_quantization_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "launch_quantization".

 C++ signature :
  bool launch_quantization_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def legato_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "legato".

 C++ signature :
  bool legato_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def loop_end_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "loop_end".

 C++ signature :
  bool loop_end_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def loop_jump_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "loop_jump".

 C++ signature :
  bool loop_jump_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def loop_start_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "loop_start".

 C++ signature :
  bool loop_start_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def looping_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "looping".

 C++ signature :
  bool looping_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def move_playing_pos(self, arg2: float) -> None:
            """
            Jump forward or backward by the specified relative amount in beats.
 Will do nothing, if the Clip is not playing.

 C++ signature :
  void move_playing_pos(TPyHandle<AClip>,double)
            :param arg2: arg2
            :type arg2: float
            :rtype: None
            """
            pass

        def move_warp_marker(self, marker_beat_time: float, beat_time_distance: float) -> None:
            """
            Available for AudioClips only.
 Moves the specified warp marker by the specified beat time amount, if possible.

 C++ signature :
  void move_warp_marker(TPyHandle<AClip>,double,double)
            :param marker_beat_time: marker_beat_time
            :type marker_beat_time: float
            :param beat_time_distance: beat_time_distance
            :type beat_time_distance: float
            :rtype: None
            """
            pass

        def muted_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "muted".

 C++ signature :
  bool muted_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def note_number_to_name(self, midi_pitch: int) -> str:
            """
            Return a human-readable name for the given MIDI note number.
 Takes into account the scale and tonal spelling settings of the clip,
 as well as the current tuning system (if any)

 C++ signature :
  TString note_number_to_name(TPyHandle<AClip>,int)
            :param midi_pitch: midi_pitch
            :type midi_pitch: int
            :rtype: str
            """
            pass

        def notes_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "notes".

 C++ signature :
  bool notes_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_coarse_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_coarse".

 C++ signature :
  bool pitch_coarse_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_fine_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_fine".

 C++ signature :
  bool pitch_fine_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playing_position_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playing_position".

 C++ signature :
  bool playing_position_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playing_status_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playing_status".

 C++ signature :
  bool playing_status_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def position_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "position".

 C++ signature :
  bool position_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def quantize(self, arg2: int, arg3: float) -> None:
            """
            Quantize all notes in a clip or align warp markers.

 C++ signature :
  void quantize(TPyHandle<AClip>,int,float)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: float
            :rtype: None
            """
            pass

        def quantize_pitch(self, arg2: int, arg3: int, arg4: float) -> None:
            """
            Quantize all the notes of a given pitch.  Raises an error on audio clips.

 C++ signature :
  void quantize_pitch(TPyHandle<AClip>,int,int,float)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :param arg4: arg4
            :type arg4: float
            :rtype: None
            """
            pass

        def ram_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ram_mode".

 C++ signature :
  bool ram_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_color_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color_index".

 C++ signature :
  void remove_color_index_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color".

 C++ signature :
  void remove_color_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_end_marker_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "end_marker".

 C++ signature :
  void remove_end_marker_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_end_time_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "end_time".

 C++ signature :
  void remove_end_time_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_file_path_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "file_path".

 C++ signature :
  void remove_file_path_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_gain_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "gain".

 C++ signature :
  void remove_gain_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_groove_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "groove".

 C++ signature :
  void remove_groove_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_has_envelopes_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "has_envelopes".

 C++ signature :
  void remove_has_envelopes_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_overdubbing_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_overdubbing".

 C++ signature :
  void remove_is_overdubbing_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_recording_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_recording".

 C++ signature :
  void remove_is_recording_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_launch_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "launch_mode".

 C++ signature :
  void remove_launch_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_launch_quantization_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "launch_quantization".

 C++ signature :
  void remove_launch_quantization_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_legato_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "legato".

 C++ signature :
  void remove_legato_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_loop_end_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "loop_end".

 C++ signature :
  void remove_loop_end_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_loop_jump_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "loop_jump".

 C++ signature :
  void remove_loop_jump_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_loop_start_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "loop_start".

 C++ signature :
  void remove_loop_start_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_looping_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "looping".

 C++ signature :
  void remove_looping_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_muted_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "muted".

 C++ signature :
  void remove_muted_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_notes(self, arg2: float, arg3: int, arg4: float, arg5: int) -> None:
            """
            Delete all notes starting in the given pitch- and time range.

 C++ signature :
  void remove_notes(TPyHandle<AClip>,double,int,double,int)
            :param arg2: arg2
            :type arg2: float
            :param arg3: arg3
            :type arg3: int
            :param arg4: arg4
            :type arg4: float
            :param arg5: arg5
            :type arg5: int
            :rtype: None
            """
            pass

        def remove_notes_by_id(self, arg2: object) -> None:
            """
            Delete all notes matching the given note IDs.
 This function should NOT be used to implement modification of existing notes
 (i.e. in combination with add_new_notes), as that leads to loss of per-note
 events. apply_note_modifications must be used instead for modifying existing
 notes.

 C++ signature :
  void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> None:
            """
            Delete all notes starting in the given pitch and time range.
 This function should NOT be used to implement modification of existing notes
 (i.e. in combination with add_new_notes), as that leads to loss of per-note
 events. apply_note_modifications must be used instead for modifying existing
 notes.

 C++ signature :
  void remove_notes_extended(TPyHandle<AClip>,int,int,double,double)
            :param from_pitch: from_pitch
            :type from_pitch: int
            :param pitch_span: pitch_span
            :type pitch_span: int
            :param from_time: from_time
            :type from_time: float
            :param time_span: time_span
            :type time_span: float
            :rtype: None
            """
            pass

        def remove_notes_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "notes".

 C++ signature :
  void remove_notes_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_coarse_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_coarse".

 C++ signature :
  void remove_pitch_coarse_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_fine_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_fine".

 C++ signature :
  void remove_pitch_fine_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playing_position_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playing_position".

 C++ signature :
  void remove_playing_position_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playing_status_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playing_status".

 C++ signature :
  void remove_playing_status_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_position_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "position".

 C++ signature :
  void remove_position_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ram_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ram_mode".

 C++ signature :
  void remove_ram_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_signature_denominator_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "signature_denominator".

 C++ signature :
  void remove_signature_denominator_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_signature_numerator_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "signature_numerator".

 C++ signature :
  void remove_signature_numerator_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_start_marker_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "start_marker".

 C++ signature :
  void remove_start_marker_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_velocity_amount_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "velocity_amount".

 C++ signature :
  void remove_velocity_amount_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warp_marker(self, beat_time: float) -> None:
            """
            Available for AudioClips only.
 Removes the specified warp marker, if possible.

 C++ signature :
  void remove_warp_marker(TPyHandle<AClip>,double)
            :param beat_time: beat_time
            :type beat_time: float
            :rtype: None
            """
            pass

        def remove_warp_markers_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warp_markers".

 C++ signature :
  void remove_warp_markers_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warp_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warp_mode".

 C++ signature :
  void remove_warp_mode_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warping_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warping".

 C++ signature :
  void remove_warping_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def replace_selected_notes(self, arg2: tuple) -> None:
            """
            Called with a tuple of tuples where each inner tuple represents
 a note in the same format as returned by get_selected_notes. The
 notes described that way will then be used to replace the old selection.

 C++ signature :
  void replace_selected_notes(TPyHandle<AClip>,boost::python::tuple)
            :param arg2: arg2
            :type arg2: tuple
            :rtype: None
            """
            pass

        def sample_to_beat_time(self, sample_time: float) -> float:
            """
            Available for AudioClips only.
 Converts the given sample time to beat time. Raises an error if the sample is not warped.

 C++ signature :
  double sample_to_beat_time(TPyHandle<AClip>,double)
            :param sample_time: sample_time
            :type sample_time: float
            :rtype: float
            """
            pass

        def scrub(self, scrub_position: float) -> None:
            """
            Scrubs inside a clip.
 scrub_position defines the position in beats that the scrub will start from.
 The scrub will continue until stop_scrub is called.
 Global quantization applies to the scrub's position and length.

 C++ signature :
  void scrub(TPyHandle<AClip>,double)
            :param scrub_position: scrub_position
            :type scrub_position: float
            :rtype: None
            """
            pass

        def seconds_to_sample_time(self, seconds: float) -> float:
            """
            Available for AudioClips only.
 Converts the given seconds to sample time. Raises an error if the sample is warped.

 C++ signature :
  double seconds_to_sample_time(TPyHandle<AClip>,double)
            :param seconds: seconds
            :type seconds: float
            :rtype: float
            """
            pass

        def select_all_notes(self, ) -> None:
            """
            Selects all notes present in the clip.

 C++ signature :
  void select_all_notes(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def select_notes_by_id(self, arg2: object) -> None:
            """
            Selects all notes matching the given note IDs.

 C++ signature :
  void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the clip's fire button state directly. Supports all launch modes.

 C++ signature :
  void set_fire_button_state(TPyHandle<AClip>,bool)
            :param arg2: arg2
            :type arg2: bool
            :rtype: None
            """
            pass

        def set_notes(self, arg2: tuple) -> None:
            """
            Called with a tuple of tuples where each inner tuple represents
 a note in the same format as returned by get_notes. The
 notes described that way will then be added to the clip.

 C++ signature :
  void set_notes(TPyHandle<AClip>,boost::python::tuple)
            :param arg2: arg2
            :type arg2: tuple
            :rtype: None
            """
            pass

        def signature_denominator_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "signature_denominator".

 C++ signature :
  bool signature_denominator_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def signature_numerator_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "signature_numerator".

 C++ signature :
  bool signature_numerator_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def start_marker_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "start_marker".

 C++ signature :
  bool start_marker_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def stop(self, ) -> None:
            """
            Stop playing this Clip.

 C++ signature :
  void stop(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def stop_scrub(self, ) -> None:
            """
            Stops the current scrub.

 C++ signature :
  void stop_scrub(TPyHandle<AClip>)
            :rtype: None
            """
            pass

        def velocity_amount_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "velocity_amount".

 C++ signature :
  bool velocity_amount_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warp_markers_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warp_markers".

 C++ signature :
  bool warp_markers_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warp_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warp_mode".

 C++ signature :
  bool warp_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warping_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warping".

 C++ signature :
  bool warping_has_listener(TPyHandle<AClip>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Clip.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the clip view.
                """
                pass

            @property
            def grid_is_triplet(self) -> None:
                """
                Get/set wether the grid is showing in triplet mode.
                """
                pass

            @property
            def grid_quantization(self) -> None:
                """
                Get/set clip grid quantization resolution.
                """
                pass

            def hide_envelope(self, ) -> None:
                """
                Hide the envelope view.

 C++ signature :
  void hide_envelope(TPyViewData<AClip>)
                :rtype: None
                """
                pass

            def select_envelope_parameter(self, arg2: DeviceParameter) -> None:
                """
                Select the given device parameter in the envelope view.

 C++ signature :
  void select_envelope_parameter(TPyViewData<AClip>,TPyHandle<ATimeableValue>)
                :param arg2: arg2
                :type arg2: DeviceParameter
                :rtype: None
                """
                pass

            def show_envelope(self, ) -> None:
                """
                Show the envelope view.

 C++ signature :
  void show_envelope(TPyViewData<AClip>)
                :rtype: None
                """
                pass

            def show_loop(self, ) -> None:
                """
                Show the entire loop in the detail view.

 C++ signature :
  void show_loop(TPyViewData<AClip>)
                :rtype: None
                """
                pass

    class ClipLaunchQuantization(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class GridQuantization(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class LaunchMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class MidiNote(object):
        def __init__(self, *a, **k):
            """
            An object representing a MIDI Note
            """
            pass

        @property
        def duration(self) -> None:
            pass

        @property
        def mute(self) -> None:
            pass

        @property
        def note_id(self) -> None:
            """
            A numerical ID that's unique within the originating clip of the note. Not to be
used directly, but important for other API calls, namely apply_note_modifications.
            """
            pass

        @property
        def pitch(self) -> None:
            pass

        @property
        def probability(self) -> None:
            pass

        @property
        def release_velocity(self) -> None:
            pass

        @property
        def start_time(self) -> None:
            pass

        @property
        def velocity(self) -> None:
            pass

        @property
        def velocity_deviation(self) -> None:
            pass

    class MidiNoteSpecification(object):
        def __init__(self, *a, **k):
            """
            An object specifying the data for creating a MIDI note. To be used with the 
add_new_notes function.
            """
            pass

    class MidiNoteVector(object):
        def __init__(self, *a, **k):
            """
            A container for holding MIDI notes from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class WarpMarker(object):
        def __init__(self, *a, **k):
            """
            This class represents a WarpMarker type.
            """
            pass

        @property
        def beat_time(self) -> None:
            """
            A WarpMarker's beat time.
            """
            pass

        @property
        def sample_time(self) -> None:
            """
            A WarpMarker's sample time.
            """
            pass

    class WarpMarkerVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning warp markers from Live.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class WarpMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class ClipSlot(ModuleType):
    pass

    class ClipSlot(object):
        def __init__(self, *a, **k):
            """
            This class represents an entry in Lives Session view matrix.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the ClipSlot.
            """
            pass

        @property
        def clip(self) -> None:
            """
            Returns the Clip which this clipslots currently owns. Might be None.
            """
            pass

        @property
        def color(self) -> None:
            """
            Returns the canonical color for the clip slot or None if it does not exist.
            """
            pass

        @property
        def color_index(self) -> None:
            """
            Returns the canonical color index for the clip slot or None if it does not exist.
            """
            pass

        @property
        def controls_other_clips(self) -> None:
            """
            Returns true if firing this slot will fire clips in other slots.
Can only be true for slots in group tracks.
            """
            pass

        @property
        def has_clip(self) -> None:
            """
            Returns true if this Clipslot owns a Clip.
            """
            pass

        @property
        def has_stop_button(self) -> None:
            """
            Get/Set if this Clip has a stop button, which will, if fired, stop any
other Clip that is currently playing the Track we do belong to.
            """
            pass

        @property
        def is_group_slot(self) -> None:
            """
            Returns whether this clip slot is a group track slot (group slot).
            """
            pass

        @property
        def is_playing(self) -> None:
            """
            Returns whether the clip associated with the slot is playing.
            """
            pass

        @property
        def is_recording(self) -> None:
            """
            Returns whether the clip associated with the slot is recording.
            """
            pass

        @property
        def is_triggered(self) -> None:
            """
            Const access to the triggering state of the clip slot.
            """
            pass

        @property
        def playing_status(self) -> None:
            """
            Const access to the playing state of the clip slot.
Can be either stopped, playing, or recording.
            """
            pass

        @property
        def will_record_on_start(self) -> None:
            """
            returns true if the clip slot will record on being fired.
            """
            pass

        def add_color_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color_index" has changed.

 C++ signature :
  void add_color_index_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color" has changed.

 C++ signature :
  void add_color_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_controls_other_clips_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "controls_other_clips" has changed.

 C++ signature :
  void add_controls_other_clips_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_has_clip_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "has_clip" has changed.

 C++ signature :
  void add_has_clip_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_has_stop_button_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "has_stop_button" has changed.

 C++ signature :
  void add_has_stop_button_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_triggered_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_triggered" has changed.

 C++ signature :
  void add_is_triggered_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playing_status_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playing_status" has changed.

 C++ signature :
  void add_playing_status_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def color_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color".

 C++ signature :
  bool color_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color_index".

 C++ signature :
  bool color_index_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def controls_other_clips_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "controls_other_clips".

 C++ signature :
  bool controls_other_clips_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def create_audio_clip(self, arg2: object) -> Clip:
            """
            Creates an audio clip referencing the file at the given absolute path in the slot.
 Throws an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.

 C++ signature :
  TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<AGroupAndClipSlotBase>,TString)
            :param arg2: arg2
            :type arg2: object
            :rtype: Clip
            """
            pass

        def create_clip(self, arg2: float) -> Clip:
            """
            Creates an empty clip with the given length in the slot.
 Throws an error when called on non-empty slots or slots in non-MIDI tracks.

 C++ signature :
  TWeakPtr<TPyHandle<AClip>> create_clip(TPyHandle<AGroupAndClipSlotBase>,double)
            :param arg2: arg2
            :type arg2: float
            :rtype: Clip
            """
            pass

        def delete_clip(self, ) -> None:
            """
            Removes the clip contained in the slot.
 Raises an exception if the slot was empty.

 C++ signature :
  void delete_clip(TPyHandle<AGroupAndClipSlotBase>)
            :rtype: None
            """
            pass

        def duplicate_clip_to(self, arg2: ClipSlot) -> None:
            """
            Duplicates the slot's clip to the passed in target slot.
 Overrides the target's clip if it's not empty.
 Raises an exception if the (source) slot itself is empty, or if source and
 target have different track types (audio vs. MIDI). Also raises if the source
 or target slot is in a group track (so called group slot).

 C++ signature :
  void duplicate_clip_to(TPyHandle<AGroupAndClipSlotBase>,TPyHandle<AGroupAndClipSlotBase>)
            :param arg2: arg2
            :type arg2: ClipSlot
            :rtype: None
            """
            pass

        def fire(self, ) -> None:
            """
            Fire a Clip if this Clipslot owns one, else trigger the stop button,
 if we have one.

 C++ signature :
  void fire(TPyHandle<AGroupAndClipSlotBase>)

fire( (ClipSlot)self [, (float)record_length=1.7976931348623157e+308 [, (int)launch_quantization=-2147483648 [, (bool)force_legato=False]]]) -> None :
 If 'record_length' is passed, the clip will be refired after the given recording length.  Raises an error if the slot owns a clip.
 'launch_quantization' determines the quantization of global transport that is applied overriding the value in the song.
 'force_legato' will make the clip play inmediatelly. The playhead will be moved to keep the clip synchronized.

 C++ signature :
  void fire(TPyHandle<AGroupAndClipSlotBase> [,double=1.7976931348623157e+308 [,int=-2147483648 [,bool=False]]])
            :rtype: None
            """
            pass

        def has_clip_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "has_clip".

 C++ signature :
  bool has_clip_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def has_stop_button_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "has_stop_button".

 C++ signature :
  bool has_stop_button_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_triggered_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_triggered".

 C++ signature :
  bool is_triggered_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playing_status_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playing_status".

 C++ signature :
  bool playing_status_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_color_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color_index".

 C++ signature :
  void remove_color_index_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color".

 C++ signature :
  void remove_color_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_controls_other_clips_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "controls_other_clips".

 C++ signature :
  void remove_controls_other_clips_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_has_clip_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "has_clip".

 C++ signature :
  void remove_has_clip_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_has_stop_button_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "has_stop_button".

 C++ signature :
  void remove_has_stop_button_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_triggered_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_triggered".

 C++ signature :
  void remove_is_triggered_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playing_status_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playing_status".

 C++ signature :
  void remove_playing_status_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the clipslot's fire button state directly. Supports all launch modes.

 C++ signature :
  void set_fire_button_state(TPyHandle<AGroupAndClipSlotBase>,bool)
            :param arg2: arg2
            :type arg2: bool
            :rtype: None
            """
            pass

        def stop(self, ) -> None:
            """
            Stop playing the contained Clip, if there is a Clip and its currently
 playing.

 C++ signature :
  void stop(TPyHandle<AGroupAndClipSlotBase>)
            :rtype: None
            """
            pass

    class ClipSlotPlayingState(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class CompressorDevice(ModuleType):
    pass

    class CompressorDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Compressor device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def available_input_routing_channels(self) -> None:
            """
            Return a list of source channels for input routing in the sidechain.
            """
            pass

        @property
        def available_input_routing_types(self) -> None:
            """
            Return a list of source types for input routing in the sidechain.
            """
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def input_routing_channel(self) -> None:
            """
            Get and set the current source channel for input routing in the sidechain.
Raises ValueError if the channel isn't one of the current values in
available_input_routing_channels.
            """
            pass

        @property
        def input_routing_type(self) -> None:
            """
            Get and set the current source type for input routing in the sidechain.
Raises ValueError if the type isn't one of the current values in
available_input_routing_types.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_available_input_routing_channels_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "available_input_routing_channels" has changed.

 C++ signature :
  void add_available_input_routing_channels_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_available_input_routing_types_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "available_input_routing_types" has changed.

 C++ signature :
  void add_available_input_routing_types_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_input_routing_channel_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "input_routing_channel" has changed.

 C++ signature :
  void add_input_routing_channel_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_input_routing_type_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "input_routing_type" has changed.

 C++ signature :
  void add_input_routing_type_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def available_input_routing_channels_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "available_input_routing_channels".

 C++ signature :
  bool available_input_routing_channels_has_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def available_input_routing_types_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "available_input_routing_types".

 C++ signature :
  bool available_input_routing_types_has_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def input_routing_channel_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "input_routing_channel".

 C++ signature :
  bool input_routing_channel_has_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def input_routing_type_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "input_routing_type".

 C++ signature :
  bool input_routing_type_has_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_available_input_routing_channels_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "available_input_routing_channels".

 C++ signature :
  void remove_available_input_routing_channels_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_available_input_routing_types_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "available_input_routing_types".

 C++ signature :
  void remove_available_input_routing_types_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_input_routing_channel_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "input_routing_channel".

 C++ signature :
  void remove_input_routing_channel_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_input_routing_type_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "input_routing_type".

 C++ signature :
  void remove_input_routing_type_listener(TCompressorDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class Conversions(ModuleType):
    pass

    @staticmethod
    def audio_to_midi_clip(song: Song, audio_clip: Clip, audio_to_midi_type: int) -> None:
        """
        Creates a MIDI clip in a new MIDI track with the notes extracted from the given
 audio_clip. The `audio_to_midi_type` decides which algorithm is used in
 the process. Raises error when called with an inconvertible clip or invalid
 `audio_to_midi_type`.

 C++ signature :
  void audio_to_midi_clip(TPyHandle<ASong>,TPyHandle<AClip>,int)
        :param song: song
        :type song: Song
        :param audio_clip: audio_clip
        :type audio_clip: Clip
        :param audio_to_midi_type: audio_to_midi_type
        :type audio_to_midi_type: int
        :rtype: None
        """
        pass

    @staticmethod
    def create_drum_rack_from_audio_clip(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new track with a drum rack with a simpler on the first pad with
 the specified audio clip.

 C++ signature :
  void create_drum_rack_from_audio_clip(TPyHandle<ASong>,TPyHandle<AClip>)
        :param song: song
        :type song: Song
        :param audio_clip: audio_clip
        :type audio_clip: Clip
        :rtype: None
        """
        pass

    @staticmethod
    def create_midi_track_from_drum_pad(song: Song, drum_pad: DrumPad) -> None:
        """
        Creates a new Midi track containing the specified Drum Pad's device chain.

 C++ signature :
  void create_midi_track_from_drum_pad(TPyHandle<ASong>,TPyHandle<ADrumGroupDevicePad>)
        :param song: song
        :type song: Song
        :param drum_pad: drum_pad
        :type drum_pad: DrumPad
        :rtype: None
        """
        pass

    @staticmethod
    def create_midi_track_with_simpler(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new Midi track with a simpler including the specified audio clip.

 C++ signature :
  void create_midi_track_with_simpler(TPyHandle<ASong>,TPyHandle<AClip>)
        :param song: song
        :type song: Song
        :param audio_clip: audio_clip
        :type audio_clip: Clip
        :rtype: None
        """
        pass

    @staticmethod
    def is_convertible_to_midi(song: Song, audio_clip: Clip) -> bool:
        """
        Returns whether `audio_clip` can be converted to MIDI.
 Raises error when called with a MIDI clip

 C++ signature :
  bool is_convertible_to_midi(TPyHandle<ASong>,TPyHandle<AClip>)
        :param song: song
        :type song: Song
        :param audio_clip: audio_clip
        :type audio_clip: Clip
        :rtype: bool
        """
        pass

    @staticmethod
    def move_devices_on_track_to_new_drum_rack_pad(song: Song, track_index: int) -> LomObject:
        """
        Moves the entire device chain of the track according to the track index
 onto the C1 (note 36) drum pad of a new drum rack in a new track.If the track associated with the track index does not contain any devices
 nothing changes (i.e. a new track and new drum rack are not created).

 C++ signature :
  TWeakPtr<TPyHandleBase> move_devices_on_track_to_new_drum_rack_pad(TPyHandle<ASong>,int)
        :param song: song
        :type song: Song
        :param track_index: track_index
        :type track_index: int
        :rtype: LomObject
        """
        pass

    @staticmethod
    def sliced_simpler_to_drum_rack(song: Song, simpler: SimplerDevice) -> None:
        """
        Converts the Simpler into a Drum Rack, assigning each slice to a drum pad.
 Calling it on a non-sliced simpler raises an error.

 C++ signature :
  void sliced_simpler_to_drum_rack(TPyHandle<ASong>,TSimplerDevicePyHandle)
        :param song: song
        :type song: Song
        :param simpler: simpler
        :type simpler: SimplerDevice
        :rtype: None
        """
        pass

    class AudioToMidiType(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class Device(ModuleType):
    pass

    class ATimeableValueVector(object):
        def __init__(self, *a, **k):
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<TWeakPtr<ATimeableValue>, std::__1::allocator<TWeakPtr<ATimeableValue>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<TWeakPtr<ATimeableValue>, std::__1::allocator<TWeakPtr<ATimeableValue>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

    class Device(object):
        def __init__(self, *a, **k):
            """
            This class represents a MIDI or Audio DSP-Device in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

    class DeviceType(object):
        def __init__(self, *a, **k):
            """
            The type of the device.
            """
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class DeviceIO(ModuleType):
    pass

    class DeviceIO(object):
        def __init__(self, *a, **k):
            """
            This class represents a specific input or output bus of a device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def available_routing_channels(self) -> None:
            """
            Return a list of channels for this IO endpoint.
            """
            pass

        @property
        def available_routing_types(self) -> None:
            """
            Return a list of available routing types for this IO endpoint.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the device IO.
            """
            pass

        @property
        def default_external_routing_channel_is_none(self) -> None:
            """
            Get and set whether the default routing channel for External routing types is none.
            """
            pass

        @property
        def routing_channel(self) -> None:
            """
            Get and set the current routing channel.
Raises ValueError if the channel isn't one of the current values in
available_routing_channels.
            """
            pass

        @property
        def routing_type(self) -> None:
            """
            Get and set the current routing type.
Raises ValueError if the type isn't one of the current values in
available_routing_types.
            """
            pass

        def add_available_routing_channels_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "available_routing_channels" has changed.

 C++ signature :
  void add_available_routing_channels_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_available_routing_types_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "available_routing_types" has changed.

 C++ signature :
  void add_available_routing_types_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_routing_channel_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "routing_channel" has changed.

 C++ signature :
  void add_routing_channel_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_routing_type_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "routing_type" has changed.

 C++ signature :
  void add_routing_type_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def available_routing_channels_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "available_routing_channels".

 C++ signature :
  bool available_routing_channels_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def available_routing_types_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "available_routing_types".

 C++ signature :
  bool available_routing_types_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_available_routing_channels_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "available_routing_channels".

 C++ signature :
  void remove_available_routing_channels_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_available_routing_types_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "available_routing_types".

 C++ signature :
  void remove_available_routing_types_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_routing_channel_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "routing_channel".

 C++ signature :
  void remove_routing_channel_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_routing_type_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "routing_type".

 C++ signature :
  void remove_routing_type_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def routing_channel_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "routing_channel".

 C++ signature :
  bool routing_channel_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def routing_type_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "routing_type".

 C++ signature :
  bool routing_type_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class DeviceParameter(ModuleType):
    pass

    class AutomationState(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class DeviceParameter(object):
        def __init__(self, *a, **k):
            """
            This class represents a (automatable) parameter within a MIDI or
Audio DSP-Device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def automation_state(self) -> None:
            """
            Returns state of type AutomationState.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the device parameter.
            """
            pass

        @property
        def default_value(self) -> None:
            """
            Return the default value for this parameter.  A Default value is only
available for non-quantized parameter types (see 'is_quantized').
            """
            pass

        @property
        def is_enabled(self) -> None:
            """
            Returns false if the parameter has been macro mapped or disabled by Max.
            """
            pass

        @property
        def is_quantized(self) -> None:
            """
            Returns True, if this value is a boolean or integer like switch.
Non quantized values are continues float values.
            """
            pass

        @property
        def max(self) -> None:
            """
            Returns const access to the upper value of the allowed range for
this parameter
            """
            pass

        @property
        def min(self) -> None:
            """
            Returns const access to the lower value of the allowed range for
this parameter
            """
            pass

        @property
        def name(self) -> None:
            """
            Returns const access the name of this parameter, as visible in Lives
automation choosers.
            """
            pass

        @property
        def original_name(self) -> None:
            """
            Returns const access the original name of this parameter, unaffected of
any renamings.
            """
            pass

        @property
        def short_value_items(self) -> None:
            """
            Return the list of possible values for this parameter. Like value_items, but prefers short value names if available. Raises an error if 'is_quantized' is False.
            """
            pass

        @property
        def state(self) -> Returns the state of the parameter:
            """
            - enabled - the parameter's value can be changed,
- irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,
- disabled - the parameter's value cannot be changed.
            """
            pass

        @property
        def value(self) -> None:
            """
            Get/Set the current value (as visible in the GUI) this parameter.
The value must be inside the min/max properties of this device.
            """
            pass

        @property
        def value_items(self) -> None:
            """
            Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.
            """
            pass

        def add_automation_state_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "automation_state" has changed.

 C++ signature :
  void add_automation_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_state_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "state" has changed.

 C++ signature :
  void add_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_value_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "value" has changed.

 C++ signature :
  void add_value_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def automation_state_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "automation_state".

 C++ signature :
  bool automation_state_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def begin_gesture(self, ) -> None:
            """
            Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent group -- for Sexample, when recording automation.

 C++ signature :
  void begin_gesture(TPyHandle<ATimeableValue>)
            :rtype: None
            """
            pass

        def end_gesture(self, ) -> None:
            """
            Notify the end of a modification of the parameter. See begin_gesture.

 C++ signature :
  void end_gesture(TPyHandle<ATimeableValue>)
            :rtype: None
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def re_enable_automation(self, ) -> None:
            """
            Reenable automation for this parameter.

 C++ signature :
  void re_enable_automation(TPyHandle<ATimeableValue>)
            :rtype: None
            """
            pass

        def remove_automation_state_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "automation_state".

 C++ signature :
  void remove_automation_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_state_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "state".

 C++ signature :
  void remove_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_value_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "value".

 C++ signature :
  void remove_value_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def state_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "state".

 C++ signature :
  bool state_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def str_for_value(self, arg2: float) -> str:
            """
            Return a string representation of the given value. To be used
 for display purposes only.  This value can include characters like 'db' or
 'hz', depending on the type of the parameter.

 C++ signature :
  TString str_for_value(TPyHandle<ATimeableValue>,float)
            :param arg2: arg2
            :type arg2: float
            :rtype: str
            """
            pass

        def value_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "value".

 C++ signature :
  bool value_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

    class ParameterState(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class DriftDevice(ModuleType):
    pass

    class DriftDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Drift device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def mod_matrix_filter_source_1_index(self) -> None:
            """
            Return the filter mod source 1 index
            """
            pass

        @property
        def mod_matrix_filter_source_1_list(self) -> None:
            """
            Return the filter mod source 1 list
            """
            pass

        @property
        def mod_matrix_filter_source_2_index(self) -> None:
            """
            Return the filter mod source 2 index
            """
            pass

        @property
        def mod_matrix_filter_source_2_list(self) -> None:
            """
            Return the filter mod source 2 list
            """
            pass

        @property
        def mod_matrix_lfo_source_index(self) -> None:
            """
            Return the lfo mod source index
            """
            pass

        @property
        def mod_matrix_lfo_source_list(self) -> None:
            """
            Return the lfo mod source list
            """
            pass

        @property
        def mod_matrix_pitch_source_1_index(self) -> None:
            """
            Return the pitch mod source 1 index
            """
            pass

        @property
        def mod_matrix_pitch_source_1_list(self) -> None:
            """
            Return the pitch mod source 1 list
            """
            pass

        @property
        def mod_matrix_pitch_source_2_index(self) -> None:
            """
            Return the pitch mod source 2 index
            """
            pass

        @property
        def mod_matrix_pitch_source_2_list(self) -> None:
            """
            Return the pitch mod source 2 list
            """
            pass

        @property
        def mod_matrix_shape_source_index(self) -> None:
            """
            Return the shape mod source index
            """
            pass

        @property
        def mod_matrix_shape_source_list(self) -> None:
            """
            Return the shape mod source list
            """
            pass

        @property
        def mod_matrix_source_1_index(self) -> None:
            """
            Return the custom mod source 1 index
            """
            pass

        @property
        def mod_matrix_source_1_list(self) -> None:
            """
            Return the custom mod source 1 list
            """
            pass

        @property
        def mod_matrix_source_2_index(self) -> None:
            """
            Return the custom mod source 2 index
            """
            pass

        @property
        def mod_matrix_source_2_list(self) -> None:
            """
            Return the custom mod source 2 list
            """
            pass

        @property
        def mod_matrix_source_3_index(self) -> None:
            """
            Return the custom mod source 3 index
            """
            pass

        @property
        def mod_matrix_source_3_list(self) -> None:
            """
            Return the custom mod source 3 list
            """
            pass

        @property
        def mod_matrix_target_1_index(self) -> None:
            """
            Return the custom mod target 1 index
            """
            pass

        @property
        def mod_matrix_target_1_list(self) -> None:
            """
            Return the custom mod target 1 list
            """
            pass

        @property
        def mod_matrix_target_2_index(self) -> None:
            """
            Return the custom mod target 2 index
            """
            pass

        @property
        def mod_matrix_target_2_list(self) -> None:
            """
            Return the custom mod target 2 list
            """
            pass

        @property
        def mod_matrix_target_3_index(self) -> None:
            """
            Return the custom mod target 3 index
            """
            pass

        @property
        def mod_matrix_target_3_list(self) -> None:
            """
            Return the custom mod target 3 list
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def pitch_bend_range(self) -> None:
            """
            Return the Pitch Bend Range
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        @property
        def voice_count_index(self) -> None:
            """
            Return the voice count index
            """
            pass

        @property
        def voice_count_list(self) -> None:
            """
            Return the voice count list
            """
            pass

        @property
        def voice_mode_index(self) -> None:
            """
            Return the voice mode index
            """
            pass

        @property
        def voice_mode_list(self) -> None:
            """
            Return the voice mode list
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_filter_source_1_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_filter_source_1_index" has changed.

 C++ signature :
  void add_mod_matrix_filter_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_filter_source_2_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_filter_source_2_index" has changed.

 C++ signature :
  void add_mod_matrix_filter_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_lfo_source_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_lfo_source_index" has changed.

 C++ signature :
  void add_mod_matrix_lfo_source_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_pitch_source_1_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_pitch_source_1_index" has changed.

 C++ signature :
  void add_mod_matrix_pitch_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_pitch_source_2_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_pitch_source_2_index" has changed.

 C++ signature :
  void add_mod_matrix_pitch_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_shape_source_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_shape_source_index" has changed.

 C++ signature :
  void add_mod_matrix_shape_source_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_source_1_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_source_1_index" has changed.

 C++ signature :
  void add_mod_matrix_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_source_2_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_source_2_index" has changed.

 C++ signature :
  void add_mod_matrix_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_source_3_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_source_3_index" has changed.

 C++ signature :
  void add_mod_matrix_source_3_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_target_1_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_target_1_index" has changed.

 C++ signature :
  void add_mod_matrix_target_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_target_2_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_target_2_index" has changed.

 C++ signature :
  void add_mod_matrix_target_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mod_matrix_target_3_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mod_matrix_target_3_index" has changed.

 C++ signature :
  void add_mod_matrix_target_3_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_bend_range" has changed.

 C++ signature :
  void add_pitch_bend_range_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_voice_count_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "voice_count_index" has changed.

 C++ signature :
  void add_voice_count_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_voice_mode_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "voice_mode_index" has changed.

 C++ signature :
  void add_voice_mode_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_filter_source_1_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_filter_source_1_index".

 C++ signature :
  bool mod_matrix_filter_source_1_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_filter_source_2_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_filter_source_2_index".

 C++ signature :
  bool mod_matrix_filter_source_2_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_lfo_source_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_lfo_source_index".

 C++ signature :
  bool mod_matrix_lfo_source_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_pitch_source_1_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_pitch_source_1_index".

 C++ signature :
  bool mod_matrix_pitch_source_1_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_pitch_source_2_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_pitch_source_2_index".

 C++ signature :
  bool mod_matrix_pitch_source_2_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_shape_source_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_shape_source_index".

 C++ signature :
  bool mod_matrix_shape_source_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_source_1_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_source_1_index".

 C++ signature :
  bool mod_matrix_source_1_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_source_2_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_source_2_index".

 C++ signature :
  bool mod_matrix_source_2_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_source_3_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_source_3_index".

 C++ signature :
  bool mod_matrix_source_3_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_target_1_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_target_1_index".

 C++ signature :
  bool mod_matrix_target_1_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_target_2_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_target_2_index".

 C++ signature :
  bool mod_matrix_target_2_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mod_matrix_target_3_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mod_matrix_target_3_index".

 C++ signature :
  bool mod_matrix_target_3_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_bend_range_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_bend_range".

 C++ signature :
  bool pitch_bend_range_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_filter_source_1_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_filter_source_1_index".

 C++ signature :
  void remove_mod_matrix_filter_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_filter_source_2_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_filter_source_2_index".

 C++ signature :
  void remove_mod_matrix_filter_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_lfo_source_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_lfo_source_index".

 C++ signature :
  void remove_mod_matrix_lfo_source_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_pitch_source_1_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_pitch_source_1_index".

 C++ signature :
  void remove_mod_matrix_pitch_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_pitch_source_2_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_pitch_source_2_index".

 C++ signature :
  void remove_mod_matrix_pitch_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_shape_source_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_shape_source_index".

 C++ signature :
  void remove_mod_matrix_shape_source_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_source_1_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_source_1_index".

 C++ signature :
  void remove_mod_matrix_source_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_source_2_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_source_2_index".

 C++ signature :
  void remove_mod_matrix_source_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_source_3_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_source_3_index".

 C++ signature :
  void remove_mod_matrix_source_3_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_target_1_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_target_1_index".

 C++ signature :
  void remove_mod_matrix_target_1_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_target_2_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_target_2_index".

 C++ signature :
  void remove_mod_matrix_target_2_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mod_matrix_target_3_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mod_matrix_target_3_index".

 C++ signature :
  void remove_mod_matrix_target_3_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_bend_range".

 C++ signature :
  void remove_pitch_bend_range_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_voice_count_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "voice_count_index".

 C++ signature :
  void remove_voice_count_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_voice_mode_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "voice_mode_index".

 C++ signature :
  void remove_voice_mode_index_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def voice_count_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "voice_count_index".

 C++ signature :
  bool voice_count_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def voice_mode_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "voice_mode_index".

 C++ signature :
  bool voice_mode_index_has_listener(TDriftDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class DrumCellDevice(ModuleType):
    pass

    class DrumCellDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a DrumCell device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def gain(self) -> None:
            """
            Return the Gain value
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_gain_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "gain" has changed.

 C++ signature :
  void add_gain_listener(TDrumCellDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def gain_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "gain".

 C++ signature :
  bool gain_has_listener(TDrumCellDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_gain_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "gain".

 C++ signature :
  void remove_gain_listener(TDrumCellDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class DrumChain(ModuleType):
    pass

    class DrumChain(object):
        def __init__(self, *a, **k):
            """
            This class represents a drum group device chain in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the chain.
            """
            pass

        @property
        def choke_group(self) -> None:
            """
            Access to the chain's choke group setting.
            """
            pass

        @property
        def color(self) -> None:
            """
            Access the color index of the Chain.
            """
            pass

        @property
        def color_index(self) -> None:
            """
            Access the color index of the Chain.
            """
            pass

        @property
        def devices(self) -> None:
            """
            Return const access to all available Devices that are present in the chains
            """
            pass

        @property
        def has_audio_input(self) -> None:
            """
            return True, if this Chain can be feed with an Audio signal. This is
true for all Audio Chains.
            """
            pass

        @property
        def has_audio_output(self) -> None:
            """
            return True, if this Chain sends out an Audio signal. This is
true for all Audio Chains, and MIDI chains with an Instrument.
            """
            pass

        @property
        def has_midi_input(self) -> None:
            """
            return True, if this Chain can be feed with an Audio signal. This is
true for all MIDI Chains.
            """
            pass

        @property
        def has_midi_output(self) -> None:
            """
            return True, if this Chain sends out MIDI events. This is
true for all MIDI Chains with no Instruments.
            """
            pass

        @property
        def is_auto_colored(self) -> None:
            """
            Get/set access to the auto color flag of the Chain.
If True, the Chain will always have the same color as the containing
Track or Chain.
            """
            pass

        @property
        def mixer_device(self) -> Return access to the mixer device that holds the chain's mixer parameters:
            """
            the Volume, Pan, and Sendamounts.
            """
            pass

        @property
        def mute(self) -> None:
            """
            Mute/unmute the chain.
            """
            pass

        @property
        def muted_via_solo(self) -> None:
            """
            Return const access to whether this chain is muted due to some other chain
being soloed.
            """
            pass

        @property
        def name(self) -> None:
            """
            Read/write access to the name of the Chain, as visible in the track header.
            """
            pass

        @property
        def out_note(self) -> None:
            """
            Access to the MIDI note sent to the devices in the chain.
            """
            pass

        @property
        def solo(self) -> None:
            """
            Get/Set the solo status of the chain. Note that this will not disable the
solo state of any other Chain in the same rack. If you want exclusive solo, 
you have to disable the solo state of the other Chains manually.
            """
            pass

        def add_choke_group_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "choke_group" has changed.

 C++ signature :
  void add_choke_group_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color_index" has changed.

 C++ signature :
  void add_color_index_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color" has changed.

 C++ signature :
  void add_color_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_devices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "devices" has changed.

 C++ signature :
  void add_devices_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_auto_colored_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_auto_colored" has changed.

 C++ signature :
  void add_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mute_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mute" has changed.

 C++ signature :
  void add_mute_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_muted_via_solo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "muted_via_solo" has changed.

 C++ signature :
  void add_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_out_note_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "out_note" has changed.

 C++ signature :
  void add_out_note_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_solo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "solo" has changed.

 C++ signature :
  void add_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def choke_group_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "choke_group".

 C++ signature :
  bool choke_group_has_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color".

 C++ signature :
  bool color_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color_index".

 C++ signature :
  bool color_index_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def delete_device(self, arg2: int) -> None:
            """
            Remove a device identified by its index from the chain. Throws runtime error if bad index.
 

 C++ signature :
  void delete_device(TChainPyHandle,int)
            :param arg2: arg2
            :type arg2: int
            :rtype: None
            """
            pass

        def devices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "devices".

 C++ signature :
  bool devices_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_auto_colored_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_auto_colored".

 C++ signature :
  bool is_auto_colored_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mute_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mute".

 C++ signature :
  bool mute_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def muted_via_solo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "muted_via_solo".

 C++ signature :
  bool muted_via_solo_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def out_note_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "out_note".

 C++ signature :
  bool out_note_has_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_choke_group_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "choke_group".

 C++ signature :
  void remove_choke_group_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color_index".

 C++ signature :
  void remove_color_index_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color".

 C++ signature :
  void remove_color_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_devices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "devices".

 C++ signature :
  void remove_devices_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_auto_colored_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_auto_colored".

 C++ signature :
  void remove_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mute_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mute".

 C++ signature :
  void remove_mute_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_muted_via_solo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "muted_via_solo".

 C++ signature :
  void remove_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_out_note_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "out_note".

 C++ signature :
  void remove_out_note_listener(TDrumChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_solo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "solo".

 C++ signature :
  void remove_solo_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def solo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "solo".

 C++ signature :
  bool solo_has_listener(TChainPyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class DrumPad(ModuleType):
    pass

    class DrumPad(object):
        def __init__(self, *a, **k):
            """
            This class represents a drum group device pad in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the drum pad.
            """
            pass

        @property
        def chains(self) -> None:
            """
            Return const access to the list of chains in this drum pad.
            """
            pass

        @property
        def mute(self) -> None:
            """
            Mute/unmute the pad.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return const access to the drum pad's name. It depends on the contained chains.
            """
            pass

        @property
        def note(self) -> None:
            """
            Get the MIDI note of the drum pad.
            """
            pass

        @property
        def solo(self) -> None:
            """
            Solo/unsolo the pad.
            """
            pass

        def add_chains_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "chains" has changed.

 C++ signature :
  void add_chains_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mute_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mute" has changed.

 C++ signature :
  void add_mute_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_solo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "solo" has changed.

 C++ signature :
  void add_solo_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def chains_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "chains".

 C++ signature :
  bool chains_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def delete_all_chains(self, ) -> None:
            """
            Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.

 C++ signature :
  void delete_all_chains(TPyHandle<ADrumGroupDevicePad>)
            :rtype: None
            """
            pass

        def mute_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mute".

 C++ signature :
  bool mute_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_chains_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "chains".

 C++ signature :
  void remove_chains_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mute_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mute".

 C++ signature :
  void remove_mute_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_solo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "solo".

 C++ signature :
  void remove_solo_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def solo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "solo".

 C++ signature :
  bool solo_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class Eq8Device(ModuleType):
    pass

    class EditMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class Eq8Device(object):
        def __init__(self, *a, **k):
            """
            This class represents an Eq8 device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def edit_mode(self) -> None:
            """
            Access to Eq8's edit mode.
            """
            pass

        @property
        def global_mode(self) -> None:
            """
            Access to Eq8's global mode.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def oversample(self) -> None:
            """
            Access to Eq8's oversample value.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_edit_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "edit_mode" has changed.

 C++ signature :
  void add_edit_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_global_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "global_mode" has changed.

 C++ signature :
  void add_global_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_oversample_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "oversample" has changed.

 C++ signature :
  void add_oversample_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def edit_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "edit_mode".

 C++ signature :
  bool edit_mode_has_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def global_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "global_mode".

 C++ signature :
  bool global_mode_has_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def oversample_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "oversample".

 C++ signature :
  bool oversample_has_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_edit_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "edit_mode".

 C++ signature :
  void remove_edit_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_global_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "global_mode".

 C++ signature :
  void remove_global_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_oversample_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "oversample".

 C++ signature :
  void remove_oversample_listener(TEq8DevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of an Eq8 device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            @property
            def selected_band(self) -> None:
                """
                Access to the selected filter band.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_selected_band_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "selected_band" has changed.

 C++ signature :
  void add_selected_band_listener(TEq8DevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_selected_band_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "selected_band".

 C++ signature :
  void remove_selected_band_listener(TEq8DevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def selected_band_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "selected_band".

 C++ signature :
  bool selected_band_has_listener(TEq8DevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

    class GlobalMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class Groove(ModuleType):
    pass

    class Base(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class Groove(object):
        def __init__(self, *a, **k):
            """
            This class represents a groove in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def base(self) -> None:
            """
            Get/set the groove's base grid.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the groove.
            """
            pass

        @property
        def name(self) -> None:
            """
            Read/write/listen access to the groove's name
            """
            pass

        @property
        def quantization_amount(self) -> None:
            """
            Read/write/listen access to the groove's quantization amount.
            """
            pass

        @property
        def random_amount(self) -> None:
            """
            Read/write/listen access to the groove's random amount.
            """
            pass

        @property
        def timing_amount(self) -> None:
            """
            Read/write/listen access to the groove's timing amount.
            """
            pass

        @property
        def velocity_amount(self) -> None:
            """
            Read/write/listen access to the groove's velocity amount.
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_quantization_amount_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "quantization_amount" has changed.

 C++ signature :
  void add_quantization_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_random_amount_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "random_amount" has changed.

 C++ signature :
  void add_random_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_timing_amount_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "timing_amount" has changed.

 C++ signature :
  void add_timing_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_velocity_amount_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "velocity_amount" has changed.

 C++ signature :
  void add_velocity_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def quantization_amount_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "quantization_amount".

 C++ signature :
  bool quantization_amount_has_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def random_amount_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "random_amount".

 C++ signature :
  bool random_amount_has_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_quantization_amount_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "quantization_amount".

 C++ signature :
  void remove_quantization_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_random_amount_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "random_amount".

 C++ signature :
  void remove_random_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_timing_amount_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "timing_amount".

 C++ signature :
  void remove_timing_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_velocity_amount_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "velocity_amount".

 C++ signature :
  void remove_velocity_amount_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def timing_amount_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "timing_amount".

 C++ signature :
  bool timing_amount_has_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def velocity_amount_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "velocity_amount".

 C++ signature :
  bool velocity_amount_has_listener(TPyHandle<AAbstractGroove>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class GroovePool(ModuleType):
    pass

    class GroovePool(object):
        def __init__(self, *a, **k):
            """
            This class represents the groove pool in Live.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the groove pool.
            """
            pass

        @property
        def grooves(self) -> None:
            """
            Access to the list of grooves
            """
            pass

        def add_grooves_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "grooves" has changed.

 C++ signature :
  void add_grooves_listener(TPyHandle<AGroovePool>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def grooves_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "grooves".

 C++ signature :
  bool grooves_has_listener(TPyHandle<AGroovePool>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_grooves_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "grooves".

 C++ signature :
  void remove_grooves_listener(TPyHandle<AGroovePool>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass


class HybridReverbDevice(ModuleType):
    pass

    class HybridReverbDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Hybrid Reverb device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def ir_attack_time(self) -> None:
            """
            Return the current IrAttackTime
            """
            pass

        @property
        def ir_category_index(self) -> None:
            """
            Return the current IR category index
            """
            pass

        @property
        def ir_category_list(self) -> None:
            """
            Return the current IR categories list
            """
            pass

        @property
        def ir_decay_time(self) -> None:
            """
            Return the current IrDecayTime
            """
            pass

        @property
        def ir_file_index(self) -> None:
            """
            Return the current IR file index
            """
            pass

        @property
        def ir_file_list(self) -> None:
            """
            Return the current IR file list
            """
            pass

        @property
        def ir_size_factor(self) -> None:
            """
            Return the current IrSizeFactor
            """
            pass

        @property
        def ir_time_shaping_on(self) -> None:
            """
            Return the current IrTimeShapingOn
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_ir_attack_time_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_attack_time" has changed.

 C++ signature :
  void add_ir_attack_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_category_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_category_index" has changed.

 C++ signature :
  void add_ir_category_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_decay_time_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_decay_time" has changed.

 C++ signature :
  void add_ir_decay_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_file_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_file_index" has changed.

 C++ signature :
  void add_ir_file_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_file_list_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_file_list" has changed.

 C++ signature :
  void add_ir_file_list_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_size_factor_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_size_factor" has changed.

 C++ signature :
  void add_ir_size_factor_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_ir_time_shaping_on_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "ir_time_shaping_on" has changed.

 C++ signature :
  void add_ir_time_shaping_on_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def ir_attack_time_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_attack_time".

 C++ signature :
  bool ir_attack_time_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_category_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_category_index".

 C++ signature :
  bool ir_category_index_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_decay_time_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_decay_time".

 C++ signature :
  bool ir_decay_time_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_file_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_file_index".

 C++ signature :
  bool ir_file_index_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_file_list_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_file_list".

 C++ signature :
  bool ir_file_list_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_size_factor_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_size_factor".

 C++ signature :
  bool ir_size_factor_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def ir_time_shaping_on_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "ir_time_shaping_on".

 C++ signature :
  bool ir_time_shaping_on_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_ir_attack_time_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_attack_time".

 C++ signature :
  void remove_ir_attack_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_category_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_category_index".

 C++ signature :
  void remove_ir_category_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_decay_time_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_decay_time".

 C++ signature :
  void remove_ir_decay_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_file_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_file_index".

 C++ signature :
  void remove_ir_file_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_file_list_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_file_list".

 C++ signature :
  void remove_ir_file_list_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_size_factor_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_size_factor".

 C++ signature :
  void remove_ir_size_factor_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_ir_time_shaping_on_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "ir_time_shaping_on".

 C++ signature :
  void remove_ir_time_shaping_on_listener(THybridReverbDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class Licensing(ModuleType):
    pass

    @staticmethod
    def authorization_clock_days_ahead():
        """
        Advances the current date by the number of days specified by _AuthClockDaysAhead

 C++ signature :
  int authorization_clock_days_ahead()
        """
        pass

    @staticmethod
    def get_authorization_page_url(reauthorize: bool, is_trial: bool) -> str:
        """
        Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization.

 C++ signature :
  TString get_authorization_page_url(bool,bool)
        :param reauthorize: reauthorize
        :type reauthorize: bool
        :param is_trial: is_trial
        :type is_trial: bool
        :rtype: str
        """
        pass

    @staticmethod
    def get_services_url():
        """
        Returns the URL against which service calls (e.g. for authorization) can be performed.

 C++ signature :
  std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> get_services_url()
        """
        pass

    @staticmethod
    def get_unlock_dir():
        """
        Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.

 C++ signature :
  boost::python::tuple get_unlock_dir()
        """
        pass

    @staticmethod
    def launch_web_browser(url: str) -> None:
        """
        Opens a web browser at the specified URL on the user's computer.

 C++ signature :
  void launch_web_browser(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
        :param url: url
        :type url: str
        :rtype: None
        """
        pass

    class ProgressDialog(object):
        def __init__(self, *a, **k):
            """
            A modal dialog showing a message and a progress animation.
            """
            pass

        def end_modal_loop(self, ) -> None:
            """
            C++ signature :
  void end_modal_loop(AProgressDialog {lvalue})
            :rtype: None
            """
            pass

        def run_in_modal_loop(self, ) -> None:
            """
            C++ signature :
  void run_in_modal_loop(AProgressDialog {lvalue})
            :rtype: None
            """
            pass

        def set_status_message(self, msg: str) -> None:
            """
            C++ signature :
  void set_status_message(TWeakPtr<AProgressDialog>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
            :param msg: msg
            :type msg: str
            :rtype: None
            """
            pass

    class PythonLicensingBridge(object):
        def __init__(self, *a, **k):
            """
            Interface to the internal licensing services.
            """
            pass

        @property
        def base_product_id(self) -> None:
            """
            Returns Live's current base product ID.
            """
            pass

        @property
        def in_sassafras_mode(self) -> None:
            pass

        @property
        def license_must_match_variant(self) -> None:
            """
            Returns a bool indicating if we require the license information returned by the server to match the variant of Live.
            """
            pass

        @property
        def random_number_for_trial_authorization(self) -> None:
            """
            Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed).
            """
            pass

        @property
        def set_has_unsaved_changes(self) -> None:
            """
            Returns true if the set has unsaved changes.
            """
            pass

        def authorize_with_sassafras(self, ) -> None:
            """
            C++ signature :
  void authorize_with_sassafras(APythonLicensingBridge {lvalue})
            :rtype: None
            """
            pass

        def create_new_live_set(self, ) -> None:
            """
            Creates a new live set and discards unsaved changes.

 C++ signature :
  void create_new_live_set(APythonLicensingBridge {lvalue})
            :rtype: None
            """
            pass

        def deauthenticate_user(self, ) -> None:
            """
            Deletes the current session ID.

 C++ signature :
  void deauthenticate_user(APythonLicensingBridge {lvalue})
            :rtype: None
            """
            pass

        def get_progress_dialog(self, ) -> ProgressDialog:
            """
            Retrieves an instance of ProgressDialog.

 C++ signature :
  TWeakPtr<AProgressDialog> get_progress_dialog(APythonLicensingBridge {lvalue})
            :rtype: ProgressDialog
            """
            pass

        def get_session_id(self, ) -> str:
            """
            Retrieve stored session ID.

 C++ signature :
  std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> get_session_id(APythonLicensingBridge {lvalue})
            :rtype: str
            """
            pass

        def get_startup_dialog(self, authorize_callable: object) -> (object)authorize_later_callable) -> StartupDialogServes as an entry point for the user to authorize Live on first launch. :
            """
            Retrieves an instance of the startup dialog with the passed callables connected to its buttons.

 C++ signature :
  TWeakPtr<AStartupDialog> get_startup_dialog(APythonLicensingBridge {lvalue},boost::python::api::object,boost::python::api::object)
            :param authorize_callable: authorize_callable
            :type authorize_callable: object
            :rtype: (object)authorize_later_callable) -> StartupDialogServes as an entry point for the user to authorize Live on first launch. 
            """
            pass

        def get_trial_time_left(self, ) -> str:
            """
            Returns remaining time on a trial as a formatted string.

 C++ signature :
  TString get_trial_time_left(APythonLicensingBridge {lvalue})
            :rtype: str
            """
            pass

        def load_and_convert_legacy_unlock_cfg(self, ) -> dict:
            """
            Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object.

 C++ signature :
  boost::python::dict load_and_convert_legacy_unlock_cfg(APythonLicensingBridge {lvalue})
            :rtype: dict
            """
            pass

        def process_license_response(self, license_response_lines: list) -> UnlockStatus:
            """
            Processes a list of strings, each representing a server response to a product authorization.

 C++ signature :
  TUnlockStatus process_license_response(APythonLicensingBridge {lvalue},boost::python::list)
            :param license_response_lines: license_response_lines
            :type license_response_lines: list
            :rtype: UnlockStatus
            """
            pass

        def process_trial_response(self, trial_response_line: str) -> bool:
            """
            Process the server's response to a Trial authorization.

 C++ signature :
  bool process_trial_response(APythonLicensingBridge {lvalue},std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
            :param trial_response_line: trial_response_line
            :type trial_response_line: str
            :rtype: bool
            """
            pass

        def request_exit(self, exit_code: int) -> None:
            """
            C++ signature :
  void request_exit(APythonLicensingBridge {lvalue} [,int=0])
            :param exit_code: exit_code
            :type exit_code: int
            :rtype: None
            """
            pass

        def save_current_set(self, ) -> None:
            """
            Saves the current Live session.

 C++ signature :
  void save_current_set(APythonLicensingBridge {lvalue})
            :rtype: None
            """
            pass

        def set_network_timer(self, callback: object, interval_in_ms: int) -> None:
            """
            Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.

 C++ signature :
  void set_network_timer(APythonLicensingBridge {lvalue},boost::python::api::object,int)
            :param callback: callback
            :type callback: object
            :param interval_in_ms: interval_in_ms
            :type interval_in_ms: int
            :rtype: None
            """
            pass

        def store_session_id(self, session_id: str) -> None:
            """
            Securely stores the user's session ID (aka cookie, aka credentials).

 C++ signature :
  void store_session_id(APythonLicensingBridge {lvalue},std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
            :param session_id: session_id
            :type session_id: str
            :rtype: None
            """
            pass

        class (object):
            def __init__(self, *a, **k):
                pass

            def end_modal_loop(self, ) -> None:
                """
                C++ signature :
  void end_modal_loop(AStartupDialog {lvalue})
                :rtype: None
                """
                pass

            def run_in_modal_loop(self, show_only_offline_auth_instructions: bool) -> None:
                """
                C++ signature :
  void run_in_modal_loop(AStartupDialog {lvalue},bool)
                :param show_only_offline_auth_instructions: show_only_offline_auth_instructions
                :type show_only_offline_auth_instructions: bool
                :rtype: None
                """
                pass

            def set_notification_message(self, notification_text: object, show_progress_bar: bool) -> None:
                """
                C++ signature :
  void set_notification_message(AStartupDialog {lvalue},TString,bool)
                :param notification_text: notification_text
                :type notification_text: object
                :param show_progress_bar: show_progress_bar
                :type show_progress_bar: bool
                :rtype: None
                """
                pass

    class TrialContext(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class UnlockStatus(object):
        def __init__(self, *a, **k):
            """
            Returns relevant information after unlock
            """
            pass

        @property
        def authorization_expired(self) -> None:
            pass

        @property
        def has_max_unlock_products(self) -> None:
            pass

        @property
        def temp_demo_mode(self) -> None:
            pass

        @property
        def time_limited(self) -> None:
            pass

        @property
        def unlock_error(self) -> None:
            pass

        @property
        def unlocked(self) -> None:
            pass


class Listener(ModuleType):
    pass

    class ListenerHandle(object):
        def __init__(self, *a, **k):
            """
            This class represents a Python listener when connected to a Live property.
            """
            pass

        @property
        def listener_func(self) -> None:
            """
            Returns the original function
            """
            pass

        @property
        def listener_self(self) -> None:
            """
            Returns the weak reference to original self, if it was a bound method
            """
            pass

        @property
        def name(self) -> None:
            """
            Prints the name of the property that this listener is connected to
            """
            pass

        def disconnect(self, ) -> None:
            """
            Disconnects the listener from its property

 C++ signature :
  void disconnect(LPythonRemote {lvalue})
            :rtype: None
            """
            pass

    class ListenerVector(object):
        def __init__(self, *a, **k):
            """
            A read only container for accessing a list of listeners.
            """
            pass

        def append(self, arg2: object) -> None:
            """
            C++ signature :
  void append(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def extend(self, arg2: object) -> None:
            """
            C++ signature :
  void extend(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass


class LomObject(ModuleType):
    pass

    class LomObject(object):
        def __init__(self, *a, **k):
            """
            this is the base class for an object that is accessible via the LOM
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass


class LooperDevice(ModuleType):
    pass

    class LooperDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Looper device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def loop_length(self) -> None:
            """
            The length of Looper's buffer.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def overdub_after_record(self) -> None:
            """
            If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch will be to playback without overdubbing.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def record_length_index(self) -> None:
            """
            Access to the Record Length chooser entry index.
            """
            pass

        @property
        def record_length_list(self) -> None:
            """
            Read-only access to the list of Record Length chooser entry strings.
            """
            pass

        @property
        def tempo(self) -> None:
            """
            The tempo of Looper's buffer.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_loop_length_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "loop_length" has changed.

 C++ signature :
  void add_loop_length_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_overdub_after_record_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "overdub_after_record" has changed.

 C++ signature :
  void add_overdub_after_record_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_record_length_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "record_length_index" has changed.

 C++ signature :
  void add_record_length_index_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_tempo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "tempo" has changed.

 C++ signature :
  void add_tempo_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def clear(self, ) -> None:
            """
            Erase Looper's recorded content.

 C++ signature :
  void clear(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def double_length(self, ) -> None:
            """
            Double the length of Looper's buffer.

 C++ signature :
  void double_length(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def double_speed(self, ) -> None:
            """
            Double the speed of Looper's playback.

 C++ signature :
  void double_speed(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def export_to_clip_slot(self, arg2: ClipSlot) -> None:
            """
            Export Looper's content to a Session Clip Slot.

 C++ signature :
  void export_to_clip_slot(TLooperDevicePyHandle,TPyHandle<AGroupAndClipSlotBase>)
            :param arg2: arg2
            :type arg2: ClipSlot
            :rtype: None
            """
            pass

        def half_length(self, ) -> None:
            """
            Halve the length of Looper's buffer.

 C++ signature :
  void half_length(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def half_speed(self, ) -> None:
            """
            Halve the speed of Looper's playback.

 C++ signature :
  void half_speed(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def loop_length_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "loop_length".

 C++ signature :
  bool loop_length_has_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def overdub(self, ) -> None:
            """
            Play back while adding additional layers of incoming audio.

 C++ signature :
  void overdub(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def overdub_after_record_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "overdub_after_record".

 C++ signature :
  bool overdub_after_record_has_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def play(self, ) -> None:
            """
            Play back without overdubbing.

 C++ signature :
  void play(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def record(self, ) -> None:
            """
            Record incoming audio.

 C++ signature :
  void record(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def record_length_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "record_length_index".

 C++ signature :
  bool record_length_index_has_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_loop_length_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "loop_length".

 C++ signature :
  void remove_loop_length_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_overdub_after_record_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "overdub_after_record".

 C++ signature :
  void remove_overdub_after_record_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_record_length_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "record_length_index".

 C++ signature :
  void remove_record_length_index_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_tempo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "tempo".

 C++ signature :
  void remove_tempo_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def stop(self, ) -> None:
            """
            Stop Looper's playback.

 C++ signature :
  void stop(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def tempo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "tempo".

 C++ signature :
  bool tempo_has_listener(TLooperDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def undo(self, ) -> None:
            """
            Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undooperation.

 C++ signature :
  void undo(TLooperDevicePyHandle)
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class MaxDevice(ModuleType):
    pass

    class MaxDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Max for Live device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def audio_inputs(self) -> None:
            """
            Const access to a list of all audio inputs of the device.
            """
            pass

        @property
        def audio_outputs(self) -> None:
            """
            Const access to a list of all audio outputs of the device.
            """
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def midi_inputs(self) -> None:
            """
            Const access to a list of all midi outputs of the device.
            """
            pass

        @property
        def midi_outputs(self) -> None:
            """
            Const access to a list of all midi outputs of the device.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_audio_inputs_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "audio_inputs" has changed.

 C++ signature :
  void add_audio_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_audio_outputs_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "audio_outputs" has changed.

 C++ signature :
  void add_audio_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_bank_parameters_changed_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "bank_parameters_changed" has changed.

 C++ signature :
  void add_bank_parameters_changed_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_midi_inputs_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "midi_inputs" has changed.

 C++ signature :
  void add_midi_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_midi_outputs_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "midi_outputs" has changed.

 C++ signature :
  void add_midi_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def audio_inputs_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "audio_inputs".

 C++ signature :
  bool audio_inputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def audio_outputs_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "audio_outputs".

 C++ signature :
  bool audio_outputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def bank_parameters_changed_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "bank_parameters_changed".

 C++ signature :
  bool bank_parameters_changed_has_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def get_bank_count(self, ) -> int:
            """
            Get the number of parameter banks. This is related to hardware control surfaces.

 C++ signature :
  int get_bank_count(TMaxDevicePyHandle)
            :rtype: int
            """
            pass

        def get_bank_name(self, arg2: int) -> str:
            """
            Get the name of a parameter bank given by index. This is related to hardware control surfaces.

 C++ signature :
  TString get_bank_name(TMaxDevicePyHandle,int)
            :param arg2: arg2
            :type arg2: int
            :rtype: str
            """
            pass

        def get_bank_parameters(self, arg2: int) -> list:
            """
            Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.

 C++ signature :
  boost::python::list get_bank_parameters(TMaxDevicePyHandle,int)
            :param arg2: arg2
            :type arg2: int
            :rtype: list
            """
            pass

        def get_value_item_icons(self, arg2: DeviceParameter) -> list:
            """
            Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.

 C++ signature :
  boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)
            :param arg2: arg2
            :type arg2: DeviceParameter
            :rtype: list
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def midi_inputs_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "midi_inputs".

 C++ signature :
  bool midi_inputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def midi_outputs_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "midi_outputs".

 C++ signature :
  bool midi_outputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_audio_inputs_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "audio_inputs".

 C++ signature :
  void remove_audio_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_audio_outputs_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "audio_outputs".

 C++ signature :
  void remove_audio_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_bank_parameters_changed_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "bank_parameters_changed".

 C++ signature :
  void remove_bank_parameters_changed_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_midi_inputs_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "midi_inputs".

 C++ signature :
  void remove_midi_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_midi_outputs_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "midi_outputs".

 C++ signature :
  void remove_midi_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class MeldDevice(ModuleType):
    pass

    class MeldDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Meld device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def mono_poly(self) -> None:
            """
            Returns the mode of Polyphony
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def poly_voices(self) -> None:
            """
            Return the Poly Voice count
            """
            pass

        @property
        def selected_engine(self) -> None:
            """
            Return what Voice Engine is selected
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def unison_voices(self) -> None:
            """
            Return the Unison Voice count
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_mono_poly_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "mono_poly" has changed.

 C++ signature :
  void add_mono_poly_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_poly_voices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "poly_voices" has changed.

 C++ signature :
  void add_poly_voices_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_selected_engine_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "selected_engine" has changed.

 C++ signature :
  void add_selected_engine_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_unison_voices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "unison_voices" has changed.

 C++ signature :
  void add_unison_voices_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def mono_poly_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "mono_poly".

 C++ signature :
  bool mono_poly_has_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def poly_voices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "poly_voices".

 C++ signature :
  bool poly_voices_has_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_mono_poly_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "mono_poly".

 C++ signature :
  void remove_mono_poly_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_poly_voices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "poly_voices".

 C++ signature :
  void remove_poly_voices_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_selected_engine_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "selected_engine".

 C++ signature :
  void remove_selected_engine_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_unison_voices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "unison_voices".

 C++ signature :
  void remove_unison_voices_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def selected_engine_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "selected_engine".

 C++ signature :
  bool selected_engine_has_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def unison_voices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "unison_voices".

 C++ signature :
  bool unison_voices_has_listener(TMeldDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class MidiMap(ModuleType):
    pass

    @staticmethod
    def forward_midi_cc(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool) -> bool:
        """
        C++ signature :
  bool forward_midi_cc(unsigned int,unsigned int,int,int [,bool=True])
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: int
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: int
        :param ShouldConsumeEvent: ShouldConsumeEvent
        :type ShouldConsumeEvent: bool
        :rtype: bool
        """
        pass

    @staticmethod
    def forward_midi_note(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool) -> bool:
        """
        C++ signature :
  bool forward_midi_note(unsigned int,unsigned int,int,int [,bool=True])
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: int
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: int
        :param ShouldConsumeEvent: ShouldConsumeEvent
        :type ShouldConsumeEvent: bool
        :rtype: bool
        """
        pass

    @staticmethod
    def forward_midi_pitchbend(arg1: int, arg2: int, arg3: int) -> bool:
        """
        C++ signature :
  bool forward_midi_pitchbend(unsigned int,unsigned int,int)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: int
        :param arg3: arg3
        :type arg3: int
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float) -> bool:
        """
        C++ signature :
  bool map_midi_cc(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,bool [,float=1.0])
        :param midi_map_handle: midi_map_handle
        :type midi_map_handle: int
        :param parameter: parameter
        :type parameter: DeviceParameter
        :param midi_channel: midi_channel
        :type midi_channel: int
        :param controller_number: controller_number
        :type controller_number: int
        :param map_mode: map_mode
        :type map_mode: MapMode
        :param avoid_takeover: avoid_takeover
        :type avoid_takeover: bool
        :param sensitivity: sensitivity
        :type sensitivity: float
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float) -> bool:
        """
        C++ signature :
  bool map_midi_cc_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,NPythonMidiMap::TCCFeedbackRule,bool [,float=1.0])
        :param midi_map_handle: midi_map_handle
        :type midi_map_handle: int
        :param parameter: parameter
        :type parameter: DeviceParameter
        :param midi_channel: midi_channel
        :type midi_channel: int
        :param controller_number: controller_number
        :type controller_number: int
        :param map_mode: map_mode
        :type map_mode: MapMode
        :param feedback_rule: feedback_rule
        :type feedback_rule: CCFeedbackRule
        :param avoid_takeover: avoid_takeover
        :type avoid_takeover: bool
        :param sensitivity: sensitivity
        :type sensitivity: float
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_note(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int) -> bool:
        """
        C++ signature :
  bool map_midi_note(unsigned int,TPyHandle<ATimeableValue>,int,int)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: DeviceParameter
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: int
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_note_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int, arg5: NoteFeedbackRule) -> bool:
        """
        C++ signature :
  bool map_midi_note_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NPythonMidiMap::TNoteFeedbackRule)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: DeviceParameter
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: int
        :param arg5: arg5
        :type arg5: NoteFeedbackRule
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_pitchbend(arg1: int, arg2: DeviceParameter, arg3: int, arg4: bool) -> bool:
        """
        C++ signature :
  bool map_midi_pitchbend(unsigned int,TPyHandle<ATimeableValue>,int,bool)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: DeviceParameter
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: bool
        :rtype: bool
        """
        pass

    @staticmethod
    def map_midi_pitchbend_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: PitchBendFeedbackRule, arg5: bool) -> bool:
        """
        C++ signature :
  bool map_midi_pitchbend_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,NPythonMidiMap::TPitchBendFeedbackRule,bool)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: DeviceParameter
        :param arg3: arg3
        :type arg3: int
        :param arg4: arg4
        :type arg4: PitchBendFeedbackRule
        :param arg5: arg5
        :type arg5: bool
        :rtype: bool
        """
        pass

    @staticmethod
    def send_feedback_for_parameter(arg1: int, arg2: DeviceParameter) -> None:
        """
        C++ signature :
  void send_feedback_for_parameter(unsigned int,TPyHandle<ATimeableValue>)
        :param arg1: arg1
        :type arg1: int
        :param arg2: arg2
        :type arg2: DeviceParameter
        :rtype: None
        """
        pass

    class CCFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            pass

        @property
        def cc_no(self) -> None:
            pass

        @property
        def cc_value_map(self) -> None:
            pass

        @property
        def channel(self) -> None:
            pass

        @property
        def delay_in_ms(self) -> None:
            pass

        @property
        def enabled(self) -> None:
            pass

    class MapMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class NoteFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            pass

        @property
        def channel(self) -> None:
            pass

        @property
        def delay_in_ms(self) -> None:
            pass

        @property
        def enabled(self) -> None:
            pass

        @property
        def note_no(self) -> None:
            pass

        @property
        def vel_map(self) -> None:
            pass

    class PitchBendFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            pass

        @property
        def channel(self) -> None:
            pass

        @property
        def delay_in_ms(self) -> None:
            pass

        @property
        def enabled(self) -> None:
            pass

        @property
        def value_pair_map(self) -> None:
            pass


class MixerDevice(ModuleType):
    pass

    class MixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Mixer Device in Live, which gives you
access to the Volume and Panning properties of a Track.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the mixer device.
            """
            pass

        @property
        def crossfade_assign(self) -> Player- and ReturnTracks only:
            """
            Access to the Track's Crossfade Assign State.
            """
            pass

        @property
        def crossfader(self) -> MainTrack only:
            """
            Const access to the Crossfader.
            """
            pass

        @property
        def cue_volume(self) -> MainTrack only:
            """
            Const access to the Cue Volume Parameter.
            """
            pass

        @property
        def left_split_stereo(self) -> None:
            """
            Const access to the Track's Left Split Stereo Panning Device Parameter.
            """
            pass

        @property
        def panning(self) -> None:
            """
            Const access to the Tracks Panning Device Parameter.
            """
            pass

        @property
        def panning_mode(self) -> None:
            """
            Access to the Track's Panning Mode.
            """
            pass

        @property
        def right_split_stereo(self) -> None:
            """
            Const access to the Track's Right Split Stereo Panning Device Parameter.
            """
            pass

        @property
        def sends(self) -> None:
            """
            Const access to the Tracks list of Send Amount Device Parameters.
            """
            pass

        @property
        def song_tempo(self) -> MainTrack only:
            """
            Const access to the Song's Tempo.
            """
            pass

        @property
        def track_activator(self) -> None:
            """
            Const access to the Tracks Activator Device Parameter.
            """
            pass

        @property
        def volume(self) -> None:
            """
            Const access to the Tracks Volume Device Parameter.
            """
            pass

        def add_crossfade_assign_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "crossfade_assign" has changed.

 C++ signature :
  void add_crossfade_assign_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_panning_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "panning_mode" has changed.

 C++ signature :
  void add_panning_mode_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_sends_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "sends" has changed.

 C++ signature :
  void add_sends_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def crossfade_assign_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "crossfade_assign".

 C++ signature :
  bool crossfade_assign_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def panning_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "panning_mode".

 C++ signature :
  bool panning_mode_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_crossfade_assign_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "crossfade_assign".

 C++ signature :
  void remove_crossfade_assign_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_panning_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "panning_mode".

 C++ signature :
  void remove_panning_mode_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_sends_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "sends".

 C++ signature :
  void remove_sends_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def sends_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "sends".

 C++ signature :
  bool sends_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class crossfade_assignments(object):
            def __init__(self, *a, **k):
                pass

            def from_bytes(self, *a, **k) -> None:
                """
                Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
                """
                pass

        class panning_modes(object):
            def __init__(self, *a, **k):
                pass

            def from_bytes(self, *a, **k) -> None:
                """
                Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
                """
                pass


class PluginDevice(ModuleType):
    pass

    class PluginDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a plugin device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def presets(self) -> None:
            """
            Get the list of presets the plugin offers.
            """
            pass

        @property
        def selected_preset_index(self) -> None:
            """
            Access to the index of the currently selected preset.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_presets_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "presets" has changed.

 C++ signature :
  void add_presets_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_selected_preset_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "selected_preset_index" has changed.

 C++ signature :
  void add_selected_preset_index_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def get_parameter_names(self, begin: int, end: int) -> StringVector:
            """
            Get the range of plugin parameter names, bound by begin and end.
 If end is smaller than 0 it is interpreted as the parameter count.
 

 C++ signature :
  std::__1::vector<TString, std::__1::allocator<TString>> get_parameter_names(TPluginDevicePyHandle [,int=0 [,int=-1]])
            :param begin: begin
            :type begin: int
            :param end: end
            :type end: int
            :rtype: StringVector
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def presets_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "presets".

 C++ signature :
  bool presets_has_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_presets_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "presets".

 C++ signature :
  void remove_presets_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_selected_preset_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "selected_preset_index".

 C++ signature :
  void remove_selected_preset_index_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def selected_preset_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "selected_preset_index".

 C++ signature :
  bool selected_preset_index_has_listener(TPluginDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class RackDevice(ModuleType):
    pass

    class RackDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Rack device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def can_show_chains(self) -> None:
            """
            return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def chain_selector(self) -> None:
            """
            Const access to the chain selector parameter.
            """
            pass

        @property
        def chains(self) -> None:
            """
            Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def drum_pads(self) -> None:
            """
            Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            pass

        @property
        def has_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.
            """
            pass

        @property
        def has_macro_mappings(self) -> None:
            """
            Returns true if any of the rack's macros are mapped to a parameter.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def is_showing_chains(self) -> None:
            """
            Returns True, if it is showing chains.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def macros_mapped(self) -> None:
            """
            A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def return_chains(self) -> None:
            """
            Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.
            """
            pass

        @property
        def selected_variation_index(self) -> None:
            """
            Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def variation_count(self) -> None:
            """
            Access to the number of macro variations currently stored.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        @property
        def visible_drum_pads(self) -> None:
            """
            Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            pass

        @property
        def visible_macro_count(self) -> None:
            """
            Access to the number of macros that are currently visible.
            """
            pass

        def add_chains_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "chains" has changed.

 C++ signature :
  void add_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_drum_pads_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "drum_pads" has changed.

 C++ signature :
  void add_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_has_drum_pads_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "has_drum_pads" has changed.

 C++ signature :
  void add_has_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_has_macro_mappings_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "has_macro_mappings" has changed.

 C++ signature :
  void add_has_macro_mappings_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_showing_chains_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_showing_chains" has changed.

 C++ signature :
  void add_is_showing_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_macro(self, ) -> None:
            """
            Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls is reached.

 C++ signature :
  void add_macro(TRackDevicePyHandle)
            :rtype: None
            """
            pass

        def add_macros_mapped_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "macros_mapped" has changed.

 C++ signature :
  void add_macros_mapped_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_return_chains_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "return_chains" has changed.

 C++ signature :
  void add_return_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_variation_count_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "variation_count" has changed.

 C++ signature :
  void add_variation_count_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_visible_drum_pads_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "visible_drum_pads" has changed.

 C++ signature :
  void add_visible_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_visible_macro_count_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "visible_macro_count" has changed.

 C++ signature :
  void add_visible_macro_count_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def chains_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "chains".

 C++ signature :
  bool chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def copy_pad(self, arg2: int, arg3: int) -> None:
            """
            Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.

 C++ signature :
  void copy_pad(TRackDevicePyHandle,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def delete_selected_variation(self, ) -> None:
            """
            Deletes the currently selected macro variation.Does nothing if there is no selected variation.

 C++ signature :
  void delete_selected_variation(TPyHandle<ADevice>)
            :rtype: None
            """
            pass

        def drum_pads_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "drum_pads".

 C++ signature :
  bool drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def has_drum_pads_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "has_drum_pads".

 C++ signature :
  bool has_drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def has_macro_mappings_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "has_macro_mappings".

 C++ signature :
  bool has_macro_mappings_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_showing_chains_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_showing_chains".

 C++ signature :
  bool is_showing_chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def macros_mapped_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "macros_mapped".

 C++ signature :
  bool macros_mapped_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def randomize_macros(self, ) -> None:
            """
            Randomizes the values for all macro controls not excluded from randomization.

 C++ signature :
  void randomize_macros(TRackDevicePyHandle)
            :rtype: None
            """
            pass

        def recall_last_used_variation(self, ) -> None:
            """
            Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.

 C++ signature :
  void recall_last_used_variation(TPyHandle<ADevice>)
            :rtype: None
            """
            pass

        def recall_selected_variation(self, ) -> None:
            """
            Recalls the currently selected macro variation.Does nothing if there are no variations.

 C++ signature :
  void recall_selected_variation(TPyHandle<ADevice>)
            :rtype: None
            """
            pass

        def remove_chains_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "chains".

 C++ signature :
  void remove_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_drum_pads_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "drum_pads".

 C++ signature :
  void remove_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_has_drum_pads_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "has_drum_pads".

 C++ signature :
  void remove_has_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_has_macro_mappings_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "has_macro_mappings".

 C++ signature :
  void remove_has_macro_mappings_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_showing_chains_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_showing_chains".

 C++ signature :
  void remove_is_showing_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_macro(self, ) -> None:
            """
            Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls is reached.

 C++ signature :
  void remove_macro(TRackDevicePyHandle)
            :rtype: None
            """
            pass

        def remove_macros_mapped_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "macros_mapped".

 C++ signature :
  void remove_macros_mapped_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_return_chains_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "return_chains".

 C++ signature :
  void remove_return_chains_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_variation_count_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "variation_count".

 C++ signature :
  void remove_variation_count_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_visible_drum_pads_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "visible_drum_pads".

 C++ signature :
  void remove_visible_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_visible_macro_count_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "visible_macro_count".

 C++ signature :
  void remove_visible_macro_count_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def return_chains_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "return_chains".

 C++ signature :
  bool return_chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def store_variation(self, ) -> None:
            """
            Stores a new variation of the values of all currently mapped macros

 C++ signature :
  void store_variation(TPyHandle<ADevice>)
            :rtype: None
            """
            pass

        def variation_count_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "variation_count".

 C++ signature :
  bool variation_count_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def visible_drum_pads_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "visible_drum_pads".

 C++ signature :
  bool visible_drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def visible_macro_count_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "visible_macro_count".

 C++ signature :
  bool visible_macro_count_has_listener(TRackDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a rack device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def drum_pads_scroll_position(self) -> None:
                """
                Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            @property
            def is_showing_chain_devices(self) -> None:
                """
                Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is false.
                """
                pass

            @property
            def selected_chain(self) -> None:
                """
                Return access to the currently selected chain.
                """
                pass

            @property
            def selected_drum_pad(self) -> None:
                """
                Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
                """
                pass

            def add_drum_pads_scroll_position_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "drum_pads_scroll_position" has changed.

 C++ signature :
  void add_drum_pads_scroll_position_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_is_showing_chain_devices_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_showing_chain_devices" has changed.

 C++ signature :
  void add_is_showing_chain_devices_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_selected_chain_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "selected_chain" has changed.

 C++ signature :
  void add_selected_chain_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_selected_drum_pad_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "selected_drum_pad" has changed.

 C++ signature :
  void add_selected_drum_pad_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def drum_pads_scroll_position_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "drum_pads_scroll_position".

 C++ signature :
  bool drum_pads_scroll_position_has_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def is_showing_chain_devices_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_showing_chain_devices".

 C++ signature :
  bool is_showing_chain_devices_has_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_drum_pads_scroll_position_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "drum_pads_scroll_position".

 C++ signature :
  void remove_drum_pads_scroll_position_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_is_showing_chain_devices_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_showing_chain_devices".

 C++ signature :
  void remove_is_showing_chain_devices_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_selected_chain_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "selected_chain".

 C++ signature :
  void remove_selected_chain_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_selected_drum_pad_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "selected_drum_pad".

 C++ signature :
  void remove_selected_drum_pad_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def selected_chain_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "selected_chain".

 C++ signature :
  bool selected_chain_has_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def selected_drum_pad_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "selected_drum_pad".

 C++ signature :
  bool selected_drum_pad_has_listener(TRackDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass


class RoarDevice(ModuleType):
    pass

    class RoarDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Roar device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def env_listen(self) -> None:
            """
            Return the Envelope Input Listen toggle state
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def routing_mode_index(self) -> None:
            """
            Return the routing mode index
            """
            pass

        @property
        def routing_mode_list(self) -> None:
            """
            Return the routing mode list
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_env_listen_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "env_listen" has changed.

 C++ signature :
  void add_env_listen_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_routing_mode_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "routing_mode_index" has changed.

 C++ signature :
  void add_routing_mode_index_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def env_listen_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "env_listen".

 C++ signature :
  bool env_listen_has_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_env_listen_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "env_listen".

 C++ signature :
  void remove_env_listen_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_routing_mode_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "routing_mode_index".

 C++ signature :
  void remove_routing_mode_index_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def routing_mode_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "routing_mode_index".

 C++ signature :
  bool routing_mode_index_has_listener(TRoarDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class Sample(ModuleType):
    pass

    class Sample(object):
        def __init__(self, *a, **k):
            """
            This class represents a sample file loaded into a Simpler instance.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def beats_granulation_resolution(self) -> None:
            """
            Access to the Granulation Resolution parameter in Beats Warp Mode.
            """
            pass

        @property
        def beats_transient_envelope(self) -> None:
            """
            Access to the Transient Envelope parameter in Beats Warp Mode.
            """
            pass

        @property
        def beats_transient_loop_mode(self) -> None:
            """
            Access to the Transient Loop Mode parameter in Beats Warp Mode.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Access to the sample's canonical parent.
            """
            pass

        @property
        def complex_pro_envelope(self) -> None:
            """
            Access to the Envelope parameter in Complex Pro Mode.
            """
            pass

        @property
        def complex_pro_formants(self) -> None:
            """
            Access to the Formants parameter in Complex Pro Warp Mode.
            """
            pass

        @property
        def end_marker(self) -> None:
            """
            Access to the position of the sample's end marker.
            """
            pass

        @property
        def file_path(self) -> None:
            """
            Get the path of the sample file.
            """
            pass

        @property
        def gain(self) -> None:
            """
            Access to the sample gain.
            """
            pass

        @property
        def length(self) -> None:
            """
            Get the length of the sample file in sample frames.
            """
            pass

        @property
        def sample_rate(self) -> None:
            """
            Access to the audio sample rate of the sample.
            """
            pass

        @property
        def slices(self) -> None:
            """
            Access to the list of slice points in sample time in the sample.
            """
            pass

        @property
        def slicing_beat_division(self) -> None:
            """
            Access to sample's slicing step size.
            """
            pass

        @property
        def slicing_region_count(self) -> None:
            """
            Access to sample's slicing split count.
            """
            pass

        @property
        def slicing_sensitivity(self) -> None:
            """
            Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.
The higher the sensitivity, the more slices will be available.
            """
            pass

        @property
        def slicing_style(self) -> None:
            """
            Access to sample's slicing style.
            """
            pass

        @property
        def start_marker(self) -> None:
            """
            Access to the position of the sample's start marker.
            """
            pass

        @property
        def texture_flux(self) -> None:
            """
            Access to the Flux parameter in Texture Warp Mode.
            """
            pass

        @property
        def texture_grain_size(self) -> None:
            """
            Access to the Grain Size parameter in Texture Warp Mode.
            """
            pass

        @property
        def tones_grain_size(self) -> None:
            """
            Access to the Grain Size parameter in Tones Warp Mode.
            """
            pass

        @property
        def warp_markers(self) -> None:
            """
            Get the warp markers for this sample.
            """
            pass

        @property
        def warp_mode(self) -> None:
            """
            Access to the sample's warp mode.
            """
            pass

        @property
        def warping(self) -> None:
            """
            Access to the sample's warping property.
            """
            pass

        def add_beats_granulation_resolution_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "beats_granulation_resolution" has changed.

 C++ signature :
  void add_beats_granulation_resolution_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_beats_transient_envelope_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "beats_transient_envelope" has changed.

 C++ signature :
  void add_beats_transient_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_beats_transient_loop_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "beats_transient_loop_mode" has changed.

 C++ signature :
  void add_beats_transient_loop_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_complex_pro_envelope_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "complex_pro_envelope" has changed.

 C++ signature :
  void add_complex_pro_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_complex_pro_formants_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "complex_pro_formants" has changed.

 C++ signature :
  void add_complex_pro_formants_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_end_marker_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "end_marker" has changed.

 C++ signature :
  void add_end_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_file_path_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "file_path" has changed.

 C++ signature :
  void add_file_path_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_gain_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "gain" has changed.

 C++ signature :
  void add_gain_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slices" has changed.

 C++ signature :
  void add_slices_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slicing_beat_division_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slicing_beat_division" has changed.

 C++ signature :
  void add_slicing_beat_division_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slicing_region_count_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slicing_region_count" has changed.

 C++ signature :
  void add_slicing_region_count_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slicing_sensitivity_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slicing_sensitivity" has changed.

 C++ signature :
  void add_slicing_sensitivity_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slicing_style_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slicing_style" has changed.

 C++ signature :
  void add_slicing_style_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_start_marker_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "start_marker" has changed.

 C++ signature :
  void add_start_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_texture_flux_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "texture_flux" has changed.

 C++ signature :
  void add_texture_flux_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_texture_grain_size_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "texture_grain_size" has changed.

 C++ signature :
  void add_texture_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_tones_grain_size_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "tones_grain_size" has changed.

 C++ signature :
  void add_tones_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warp_markers_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warp_markers" has changed.

 C++ signature :
  void add_warp_markers_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warp_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warp_mode" has changed.

 C++ signature :
  void add_warp_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_warping_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "warping" has changed.

 C++ signature :
  void add_warping_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def beat_to_sample_time(self, beat_time: float) -> float:
            """
            Converts the given beat time to sample time. Raises an error if the sample is not warped.

 C++ signature :
  double beat_to_sample_time(TPyHandle<AMultiSamplePart>,double)
            :param beat_time: beat_time
            :type beat_time: float
            :rtype: float
            """
            pass

        def beats_granulation_resolution_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "beats_granulation_resolution".

 C++ signature :
  bool beats_granulation_resolution_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def beats_transient_envelope_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "beats_transient_envelope".

 C++ signature :
  bool beats_transient_envelope_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def beats_transient_loop_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "beats_transient_loop_mode".

 C++ signature :
  bool beats_transient_loop_mode_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def clear_slices(self, ) -> None:
            """
            Clears all slices created in Simpler's manual mode.

 C++ signature :
  void clear_slices(TPyHandle<AMultiSamplePart>)
            :rtype: None
            """
            pass

        def complex_pro_envelope_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "complex_pro_envelope".

 C++ signature :
  bool complex_pro_envelope_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def complex_pro_formants_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "complex_pro_formants".

 C++ signature :
  bool complex_pro_formants_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def end_marker_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "end_marker".

 C++ signature :
  bool end_marker_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def file_path_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "file_path".

 C++ signature :
  bool file_path_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def gain_display_string(self, ) -> str:
            """
            Get the gain's display value as a string.

 C++ signature :
  TString gain_display_string(TPyHandle<AMultiSamplePart>)
            :rtype: str
            """
            pass

        def gain_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "gain".

 C++ signature :
  bool gain_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def insert_slice(self, slice_time: int) -> None:
            """
            Add a slice point at the provided time if there is none.

 C++ signature :
  void insert_slice(TPyHandle<AMultiSamplePart>,int)
            :param slice_time: slice_time
            :type slice_time: int
            :rtype: None
            """
            pass

        def move_slice(self, old_time: int, new_time: int) -> int:
            """
            Move the slice point at the provided time.

 C++ signature :
  int move_slice(TPyHandle<AMultiSamplePart>,int,int)
            :param old_time: old_time
            :type old_time: int
            :param new_time: new_time
            :type new_time: int
            :rtype: int
            """
            pass

        def remove_beats_granulation_resolution_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "beats_granulation_resolution".

 C++ signature :
  void remove_beats_granulation_resolution_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_beats_transient_envelope_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "beats_transient_envelope".

 C++ signature :
  void remove_beats_transient_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_beats_transient_loop_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "beats_transient_loop_mode".

 C++ signature :
  void remove_beats_transient_loop_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_complex_pro_envelope_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "complex_pro_envelope".

 C++ signature :
  void remove_complex_pro_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_complex_pro_formants_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "complex_pro_formants".

 C++ signature :
  void remove_complex_pro_formants_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_end_marker_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "end_marker".

 C++ signature :
  void remove_end_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_file_path_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "file_path".

 C++ signature :
  void remove_file_path_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_gain_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "gain".

 C++ signature :
  void remove_gain_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slice(self, slice_time: int) -> None:
            """
            Remove the slice point at the provided time if there is one.

 C++ signature :
  void remove_slice(TPyHandle<AMultiSamplePart>,int)
            :param slice_time: slice_time
            :type slice_time: int
            :rtype: None
            """
            pass

        def remove_slices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slices".

 C++ signature :
  void remove_slices_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slicing_beat_division_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slicing_beat_division".

 C++ signature :
  void remove_slicing_beat_division_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slicing_region_count_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slicing_region_count".

 C++ signature :
  void remove_slicing_region_count_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slicing_sensitivity_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slicing_sensitivity".

 C++ signature :
  void remove_slicing_sensitivity_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slicing_style_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slicing_style".

 C++ signature :
  void remove_slicing_style_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_start_marker_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "start_marker".

 C++ signature :
  void remove_start_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_texture_flux_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "texture_flux".

 C++ signature :
  void remove_texture_flux_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_texture_grain_size_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "texture_grain_size".

 C++ signature :
  void remove_texture_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_tones_grain_size_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "tones_grain_size".

 C++ signature :
  void remove_tones_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warp_markers_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warp_markers".

 C++ signature :
  void remove_warp_markers_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warp_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warp_mode".

 C++ signature :
  void remove_warp_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_warping_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "warping".

 C++ signature :
  void remove_warping_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def reset_slices(self, ) -> None:
            """
            Resets all edited slices to their original positions.

 C++ signature :
  void reset_slices(TPyHandle<AMultiSamplePart>)
            :rtype: None
            """
            pass

        def sample_to_beat_time(self, sample_time: float) -> float:
            """
            Converts the given sample time to beat time. Raises an error if the sample is not warped.

 C++ signature :
  double sample_to_beat_time(TPyHandle<AMultiSamplePart>,double)
            :param sample_time: sample_time
            :type sample_time: float
            :rtype: float
            """
            pass

        def slices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slices".

 C++ signature :
  bool slices_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def slicing_beat_division_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slicing_beat_division".

 C++ signature :
  bool slicing_beat_division_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def slicing_region_count_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slicing_region_count".

 C++ signature :
  bool slicing_region_count_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def slicing_sensitivity_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slicing_sensitivity".

 C++ signature :
  bool slicing_sensitivity_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def slicing_style_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slicing_style".

 C++ signature :
  bool slicing_style_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def start_marker_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "start_marker".

 C++ signature :
  bool start_marker_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def texture_flux_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "texture_flux".

 C++ signature :
  bool texture_flux_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def texture_grain_size_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "texture_grain_size".

 C++ signature :
  bool texture_grain_size_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def tones_grain_size_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "tones_grain_size".

 C++ signature :
  bool tones_grain_size_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warp_markers_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warp_markers".

 C++ signature :
  bool warp_markers_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warp_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warp_mode".

 C++ signature :
  bool warp_mode_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warping_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "warping".

 C++ signature :
  bool warping_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

    class SlicingBeatDivision(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class SlicingStyle(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class TransientLoopMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class Scene(ModuleType):
    pass

    class Scene(object):
        def __init__(self, *a, **k):
            """
            This class represents an series of ClipSlots in Lives Sessionview matrix.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the scene.
            """
            pass

        @property
        def clip_slots(self) -> None:
            """
            return a list of clipslots (see class AClipSlot) that this scene covers.
            """
            pass

        @property
        def color(self) -> None:
            """
            Get/set access to the color of the scene (RGB).
            """
            pass

        @property
        def color_index(self) -> None:
            """
            Get/set access to the color index of the scene. Can be None for no color.
            """
            pass

        @property
        def is_empty(self) -> None:
            """
            Returns True if all clip slots of this scene are empty.
            """
            pass

        @property
        def is_triggered(self) -> None:
            """
            Const access to the scene's trigger state.
            """
            pass

        @property
        def name(self) -> None:
            """
            Get/Set the name of the scene.
            """
            pass

        @property
        def tempo(self) -> None:
            """
            Get/Set the tempo value of the scene.
The song will use the scene's tempo as soon as the scene is fired.
Returns -1 if the scene has no tempo property.
            """
            pass

        @property
        def tempo_enabled(self) -> None:
            """
            Get/Set the active state of the scene tempo.
When disabled, the scene will use the song's tempo,and the tempo value returned will be -1Returns a bool indicating the state of the scene's tempo
            """
            pass

        @property
        def time_signature_denominator(self) -> None:
            """
            Get/Set the scene's time signature denominator.
The song will use the scene's time signature as soon as the scene is fired.
Returns -1 if the scene has no time signature property.
            """
            pass

        @property
        def time_signature_enabled(self) -> None:
            """
            Get the active state of the scene time signature.
When disabled, the scene will use the song's time signature,and the time signature values returned will be -1Returns a bool indicating the state of the scene's time signature
            """
            pass

        @property
        def time_signature_numerator(self) -> None:
            """
            Get/Set the scene's time signature numerator.
The song will use the scene's time signature as soon as the scene is fired.
Returns -1 if the scene has no time signature property.
            """
            pass

        def add_clip_slots_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "clip_slots" has changed.

 C++ signature :
  void add_clip_slots_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color_index" has changed.

 C++ signature :
  void add_color_index_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_color_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "color" has changed.

 C++ signature :
  void add_color_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_triggered_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_triggered" has changed.

 C++ signature :
  void add_is_triggered_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_tempo_enabled_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "tempo_enabled" has changed.

 C++ signature :
  void add_tempo_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_tempo_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "tempo" has changed.

 C++ signature :
  void add_tempo_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_time_signature_denominator_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "time_signature_denominator" has changed.

 C++ signature :
  void add_time_signature_denominator_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_time_signature_enabled_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "time_signature_enabled" has changed.

 C++ signature :
  void add_time_signature_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_time_signature_numerator_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "time_signature_numerator" has changed.

 C++ signature :
  void add_time_signature_numerator_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def clip_slots_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "clip_slots".

 C++ signature :
  bool clip_slots_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color".

 C++ signature :
  bool color_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def color_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "color_index".

 C++ signature :
  bool color_index_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def fire(self, force_legato: bool, can_select_scene_on_launch: bool) -> None:
            """
            Fire the scene directly. Will fire all clipslots that this scene owns and
 select the scene itself.

 C++ signature :
  void fire(TPyHandle<AScene> [,bool=False [,bool=True]])
            :param force_legato: force_legato
            :type force_legato: bool
            :param can_select_scene_on_launch: can_select_scene_on_launch
            :type can_select_scene_on_launch: bool
            :rtype: None
            """
            pass

        def fire_as_selected(self, force_legato: bool) -> None:
            """
            Fire the selected scene. Will fire all clipslots that this scene owns and
 select the next scene if necessary.

 C++ signature :
  void fire_as_selected(TPyHandle<AScene> [,bool=False])
            :param force_legato: force_legato
            :type force_legato: bool
            :rtype: None
            """
            pass

        def is_triggered_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_triggered".

 C++ signature :
  bool is_triggered_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_clip_slots_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "clip_slots".

 C++ signature :
  void remove_clip_slots_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color_index".

 C++ signature :
  void remove_color_index_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_color_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "color".

 C++ signature :
  void remove_color_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_triggered_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_triggered".

 C++ signature :
  void remove_is_triggered_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_tempo_enabled_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "tempo_enabled".

 C++ signature :
  void remove_tempo_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_tempo_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "tempo".

 C++ signature :
  void remove_tempo_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_time_signature_denominator_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "time_signature_denominator".

 C++ signature :
  void remove_time_signature_denominator_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_time_signature_enabled_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "time_signature_enabled".

 C++ signature :
  void remove_time_signature_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_time_signature_numerator_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "time_signature_numerator".

 C++ signature :
  void remove_time_signature_numerator_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the scene's fire button state directly. Supports all launch modes.

 C++ signature :
  void set_fire_button_state(TPyHandle<AScene>,bool)
            :param arg2: arg2
            :type arg2: bool
            :rtype: None
            """
            pass

        def tempo_enabled_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "tempo_enabled".

 C++ signature :
  bool tempo_enabled_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def tempo_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "tempo".

 C++ signature :
  bool tempo_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def time_signature_denominator_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "time_signature_denominator".

 C++ signature :
  bool time_signature_denominator_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def time_signature_enabled_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "time_signature_enabled".

 C++ signature :
  bool time_signature_enabled_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def time_signature_numerator_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "time_signature_numerator".

 C++ signature :
  bool time_signature_numerator_has_listener(TPyHandle<AScene>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass


class ShifterDevice(ModuleType):
    pass

    class ShifterDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Shifter device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def pitch_bend_range(self) -> None:
            """
            Return the pitch bend range for MIDI pitch mode
            """
            pass

        @property
        def pitch_mode_index(self) -> None:
            """
            Return the current pitch mode index
            """
            pass

        @property
        def pitch_mode_list(self) -> None:
            """
            Return the current pitch mode list
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_bend_range" has changed.

 C++ signature :
  void add_pitch_bend_range_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_mode_index_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_mode_index" has changed.

 C++ signature :
  void add_pitch_mode_index_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_bend_range_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_bend_range".

 C++ signature :
  bool pitch_bend_range_has_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_mode_index_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_mode_index".

 C++ signature :
  bool pitch_mode_index_has_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_bend_range".

 C++ signature :
  void remove_pitch_bend_range_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_mode_index_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_mode_index".

 C++ signature :
  void remove_pitch_mode_index_listener(TShifterDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass


class SimplerDevice(ModuleType):
    pass

    @staticmethod
    def get_available_voice_numbers():
        """
        Get a vector of valid Simpler voice numbers.

 C++ signature :
  std::__1::vector<int, std::__1::allocator<int>> get_available_voice_numbers()
        """
        pass

    class PlaybackMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class SimplerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Simpler device.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def can_have_chains(self) -> None:
            """
            Returns true if the device is a rack.
            """
            pass

        @property
        def can_have_drum_pads(self) -> None:
            """
            Returns true if the device is a drum rack.
            """
            pass

        @property
        def can_warp_as(self) -> None:
            """
            Returns true if warp_as is available.
            """
            pass

        @property
        def can_warp_double(self) -> None:
            """
            Returns true if warp_double is available.
            """
            pass

        @property
        def can_warp_half(self) -> None:
            """
            Returns true if warp_half is available.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the Device.
            """
            pass

        @property
        def class_display_name(self) -> None:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            pass

        @property
        def class_name(self) -> None:
            """
            Return const access to the name of the device's class.
            """
            pass

        @property
        def is_active(self) -> None:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            pass

        @property
        def latency_in_ms(self) -> None:
            """
            Returns the latency of the device in ms.
            """
            pass

        @property
        def latency_in_samples(self) -> None:
            """
            Returns the latency of the device in samples.
            """
            pass

        @property
        def multi_sample_mode(self) -> None:
            """
            Returns whether Simpler is in mulit-sample mode.
            """
            pass

        @property
        def name(self) -> None:
            """
            Return access to the name of the device.
            """
            pass

        @property
        def note_pitch_bend_range(self) -> None:
            """
            Access to the Note Pitch Bend Range in Simpler.
            """
            pass

        @property
        def pad_slicing(self) -> None:
            """
            When set to true, slices can be added in slicing mode by playing notes 
.that are not assigned to slices, yet.
            """
            pass

        @property
        def parameters(self) -> None:
            """
            Const access to the list of available automatable parameters for this device.
            """
            pass

        @property
        def pitch_bend_range(self) -> None:
            """
            Access to the Pitch Bend Range in Simpler.
            """
            pass

        @property
        def playback_mode(self) -> None:
            """
            Access to Simpler's playback mode.
            """
            pass

        @property
        def playing_position(self) -> None:
            """
            Constant access to the current playing position in the sample.
The returned value is the normalized position between sample start and end.
            """
            pass

        @property
        def playing_position_enabled(self) -> None:
            """
            Returns whether Simpler is showing the playing position.
The returned value is True while the sample is played back
            """
            pass

        @property
        def retrigger(self) -> None:
            """
            Access to Simpler's retrigger mode.
            """
            pass

        @property
        def sample(self) -> None:
            """
            Get the loaded Sample.
            """
            pass

        @property
        def slicing_playback_mode(self) -> None:
            """
            Access to Simpler's slicing playback mode.
            """
            pass

        @property
        def type(self) -> None:
            """
            Return the type of the device.
            """
            pass

        @property
        def view(self) -> None:
            """
            Representing the view aspects of a device.
            """
            pass

        @property
        def voices(self) -> None:
            """
            Access to the number of voices in Simpler.
            """
            pass

        def add_can_warp_as_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "can_warp_as" has changed.

 C++ signature :
  void add_can_warp_as_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_can_warp_double_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "can_warp_double" has changed.

 C++ signature :
  void add_can_warp_double_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_can_warp_half_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "can_warp_half" has changed.

 C++ signature :
  void add_can_warp_half_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_is_active_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "is_active" has changed.

 C++ signature :
  void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_ms" has changed.

 C++ signature :
  void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "latency_in_samples" has changed.

 C++ signature :
  void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_multi_sample_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "multi_sample_mode" has changed.

 C++ signature :
  void add_multi_sample_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_note_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "note_pitch_bend_range" has changed.

 C++ signature :
  void add_note_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pad_slicing_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pad_slicing" has changed.

 C++ signature :
  void add_pad_slicing_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_parameters_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "parameters" has changed.

 C++ signature :
  void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "pitch_bend_range" has changed.

 C++ signature :
  void add_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playback_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playback_mode" has changed.

 C++ signature :
  void add_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playing_position_enabled_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playing_position_enabled" has changed.

 C++ signature :
  void add_playing_position_enabled_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_playing_position_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "playing_position" has changed.

 C++ signature :
  void add_playing_position_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_retrigger_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "retrigger" has changed.

 C++ signature :
  void add_retrigger_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_sample_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "sample" has changed.

 C++ signature :
  void add_sample_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_slicing_playback_mode_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "slicing_playback_mode" has changed.

 C++ signature :
  void add_slicing_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_voices_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "voices" has changed.

 C++ signature :
  void add_voices_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def can_warp_as_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "can_warp_as".

 C++ signature :
  bool can_warp_as_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def can_warp_double_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "can_warp_double".

 C++ signature :
  bool can_warp_double_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def can_warp_half_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "can_warp_half".

 C++ signature :
  bool can_warp_half_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def crop(self, ) -> None:
            """
            Crop the loaded sample to the active area between start- and end marker.
 Calling this method on an empty simpler raises an error.

 C++ signature :
  void crop(TSimplerDevicePyHandle)
            :rtype: None
            """
            pass

        def guess_playback_length(self, ) -> float:
            """
            Return an estimated beat time for the playback length between start- and end-marker.
 Calling this method on an empty simpler raises an error.

 C++ signature :
  double guess_playback_length(TSimplerDevicePyHandle)
            :rtype: float
            """
            pass

        def is_active_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "is_active".

 C++ signature :
  bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_ms_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_ms".

 C++ signature :
  bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def latency_in_samples_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "latency_in_samples".

 C++ signature :
  bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def multi_sample_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "multi_sample_mode".

 C++ signature :
  bool multi_sample_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def note_pitch_bend_range_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "note_pitch_bend_range".

 C++ signature :
  bool note_pitch_bend_range_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pad_slicing_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pad_slicing".

 C++ signature :
  bool pad_slicing_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def parameters_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "parameters".

 C++ signature :
  bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def pitch_bend_range_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "pitch_bend_range".

 C++ signature :
  bool pitch_bend_range_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playback_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playback_mode".

 C++ signature :
  bool playback_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playing_position_enabled_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playing_position_enabled".

 C++ signature :
  bool playing_position_enabled_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def playing_position_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "playing_position".

 C++ signature :
  bool playing_position_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_can_warp_as_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "can_warp_as".

 C++ signature :
  void remove_can_warp_as_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_can_warp_double_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "can_warp_double".

 C++ signature :
  void remove_can_warp_double_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_can_warp_half_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "can_warp_half".

 C++ signature :
  void remove_can_warp_half_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_is_active_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "is_active".

 C++ signature :
  void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_ms_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_ms".

 C++ signature :
  void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_latency_in_samples_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "latency_in_samples".

 C++ signature :
  void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_multi_sample_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "multi_sample_mode".

 C++ signature :
  void remove_multi_sample_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_note_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "note_pitch_bend_range".

 C++ signature :
  void remove_note_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pad_slicing_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pad_slicing".

 C++ signature :
  void remove_pad_slicing_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_parameters_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "parameters".

 C++ signature :
  void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_pitch_bend_range_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "pitch_bend_range".

 C++ signature :
  void remove_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playback_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playback_mode".

 C++ signature :
  void remove_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playing_position_enabled_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playing_position_enabled".

 C++ signature :
  void remove_playing_position_enabled_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_playing_position_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "playing_position".

 C++ signature :
  void remove_playing_position_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_retrigger_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "retrigger".

 C++ signature :
  void remove_retrigger_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_sample_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "sample".

 C++ signature :
  void remove_sample_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_slicing_playback_mode_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "slicing_playback_mode".

 C++ signature :
  void remove_slicing_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_voices_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "voices".

 C++ signature :
  void remove_voices_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def retrigger_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "retrigger".

 C++ signature :
  bool retrigger_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def reverse(self, ) -> None:
            """
            Reverse the loaded sample.
 Calling this method on an empty simpler raises an error.

 C++ signature :
  void reverse(TSimplerDevicePyHandle)
            :rtype: None
            """
            pass

        def sample_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "sample".

 C++ signature :
  bool sample_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def slicing_playback_mode_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "slicing_playback_mode".

 C++ signature :
  bool slicing_playback_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.

 C++ signature :
  void store_chosen_bank(TPyHandle<ADevice>,int,int)
            :param arg2: arg2
            :type arg2: int
            :param arg3: arg3
            :type arg3: int
            :rtype: None
            """
            pass

        def voices_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "voices".

 C++ signature :
  bool voices_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def warp_as(self, beat_time: float) -> None:
            """
            Warp the playback region between start- and end-marker as the given length.
 Calling this method on an empty simpler raises an error.

 C++ signature :
  void warp_as(TSimplerDevicePyHandle,double)
            :param beat_time: beat_time
            :type beat_time: float
            :rtype: None
            """
            pass

        def warp_double(self, ) -> None:
            """
            Doubles the tempo for region between start- and end-marker.

 C++ signature :
  void warp_double(TSimplerDevicePyHandle)
            :rtype: None
            """
            pass

        def warp_half(self, ) -> None:
            """
            Halves the tempo for region between start- and end-marker.

 C++ signature :
  void warp_half(TSimplerDevicePyHandle)
            :rtype: None
            """
            pass

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a simpler device.
                """
                pass

            @property
            def _live_ptr(self) -> None:
                pass

            @property
            def canonical_parent(self) -> None:
                """
                Get the canonical parent of the View.
                """
                pass

            @property
            def is_collapsed(self) -> None:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                pass

            @property
            def sample_end(self) -> None:
                """
                Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_env_fade_in(self) -> None:
                """
                Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_env_fade_out(self) -> None:
                """
                Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_loop_end(self) -> None:
                """
                Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_loop_fade(self) -> None:
                """
                Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_loop_start(self) -> None:
                """
                Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def sample_start(self) -> None:
                """
                Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.
                """
                pass

            @property
            def selected_slice(self) -> None:
                """
                Access to the selected slice.
                """
                pass

            def add_is_collapsed_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "is_collapsed" has changed.

 C++ signature :
  void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_end_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_end" has changed.

 C++ signature :
  void add_sample_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_env_fade_in_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_env_fade_in" has changed.

 C++ signature :
  void add_sample_env_fade_in_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_env_fade_out_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_env_fade_out" has changed.

 C++ signature :
  void add_sample_env_fade_out_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_loop_end_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_loop_end" has changed.

 C++ signature :
  void add_sample_loop_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_loop_fade_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_loop_fade" has changed.

 C++ signature :
  void add_sample_loop_fade_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_loop_start_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_loop_start" has changed.

 C++ signature :
  void add_sample_loop_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_sample_start_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "sample_start" has changed.

 C++ signature :
  void add_sample_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def add_selected_slice_listener(self, arg2: object) -> None:
                """
                Add a listener function or method, which will be called as soon as the
 property "selected_slice" has changed.

 C++ signature :
  void add_selected_slice_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def is_collapsed_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "is_collapsed".

 C++ signature :
  bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def remove_is_collapsed_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "is_collapsed".

 C++ signature :
  void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_end_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_end".

 C++ signature :
  void remove_sample_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_env_fade_in_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_env_fade_in".

 C++ signature :
  void remove_sample_env_fade_in_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_env_fade_out_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_env_fade_out".

 C++ signature :
  void remove_sample_env_fade_out_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_loop_end_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_loop_end".

 C++ signature :
  void remove_sample_loop_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_loop_fade_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_loop_fade".

 C++ signature :
  void remove_sample_loop_fade_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_loop_start_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_loop_start".

 C++ signature :
  void remove_sample_loop_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_sample_start_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "sample_start".

 C++ signature :
  void remove_sample_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def remove_selected_slice_listener(self, arg2: object) -> None:
                """
                Remove a previously set listener function or method from
 property "selected_slice".

 C++ signature :
  void remove_selected_slice_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: None
                """
                pass

            def sample_end_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_end".

 C++ signature :
  bool sample_end_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_env_fade_in_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_env_fade_in".

 C++ signature :
  bool sample_env_fade_in_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_env_fade_out_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_env_fade_out".

 C++ signature :
  bool sample_env_fade_out_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_loop_end_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_loop_end".

 C++ signature :
  bool sample_loop_end_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_loop_fade_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_loop_fade".

 C++ signature :
  bool sample_loop_fade_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_loop_start_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_loop_start".

 C++ signature :
  bool sample_loop_start_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def sample_start_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "sample_start".

 C++ signature :
  bool sample_start_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

            def selected_slice_has_listener(self, arg2: object) -> bool:
                """
                Returns true, if the given listener function or method is connected
 to the property "selected_slice".

 C++ signature :
  bool selected_slice_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
                :param arg2: arg2
                :type arg2: object
                :rtype: bool
                """
                pass

    class SlicingPlaybackMode(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass


class Song(ModuleType):
    pass

    @staticmethod
    def get_all_scales_ordered():
        """
        Get an ordered tuple of tuples of all available scale names to intervals.

 C++ signature :
  boost::python::tuple get_all_scales_ordered()
        """
        pass

    class BeatTime(object):
        def __init__(self, *a, **k):
            """
            Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.
            """
            pass

        @property
        def bars(self) -> None:
            pass

        @property
        def beats(self) -> None:
            pass

        @property
        def sub_division(self) -> None:
            pass

        @property
        def ticks(self) -> None:
            pass

    class CaptureDestination(object):
        def __init__(self, *a, **k):
            """
            The destination for MIDI capture.
            """
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class CaptureMode(object):
        def __init__(self, *a, **k):
            """
            The capture mode that is used for capture and insert scene.
            """
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class CuePoint(object):
        def __init__(self, *a, **k):
            """
            Represents a 'Marker' in the arrangement.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the cue point.
            """
            pass

        @property
        def name(self) -> None:
            """
            Get/Set/Listen to the name of this CuePoint, as visible in the arranger.
            """
            pass

        @property
        def time(self) -> None:
            """
            Get/Listen to the CuePoint's time in beats.
            """
            pass

        def add_name_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "name" has changed.

 C++ signature :
  void add_name_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def add_time_listener(self, arg2: object) -> None:
            """
            Add a listener function or method, which will be called as soon as the
 property "time" has changed.

 C++ signature :
  void add_time_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def jump(self, ) -> None:
            """
            When the Song is playing, set the playing-position quantized to
 this Cuepoint's time. When not playing, simply move the start
 playing position.

 C++ signature :
  void jump(TPyHandle<ACuePoint>)
            :rtype: None
            """
            pass

        def name_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "name".

 C++ signature :
  bool name_has_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

        def remove_name_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "name".

 C++ signature :
  void remove_name_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def remove_time_listener(self, arg2: object) -> None:
            """
            Remove a previously set listener function or method from
 property "time".

 C++ signature :
  void remove_time_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: None
            """
            pass

        def time_has_listener(self, arg2: object) -> bool:
            """
            Returns true, if the given listener function or method is connected
 to the property "time".

 C++ signature :
  bool time_has_listener(TPyHandle<ACuePoint>,boost::python::api::object)
            :param arg2: arg2
            :type arg2: object
            :rtype: bool
            """
            pass

    class Quantization(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class RecordingQuantization(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class SessionRecordStatus(object):
        def __init__(self, *a, **k):
            pass

        def from_bytes(self, *a, **k) -> None:
            """
            Return the integer represented by the given array of bytes.

  bytes
 Holds the array of bytes to convert.  The argument must either
 support the buffer protocol or be an iterable object producing bytes.
 Bytes and bytearray are examples of built-in objects that support the
 buffer protocol.
  byteorder
 The byte order used to represent the integer.  If byteorder is 'big',
 the most significant byte is at the beginning of the byte array.  If
 byteorder is 'little', the most significant byte is at the end of the
 byte array.  To request the native byte order of the host system, use
 `sys.byteorder' as the byte order value.  Default is to use 'big'.
  signed
 Indicates whether two's complement is used to represent the integer.
            """
            pass

    class SmptTime(object):
        def __init__(self, *a, **k):
            """
            Represents a Time, split into Hours, Minutes, Seconds and Frames.
The frame type must be specified when calling a function that returns
a SmptTime.
            """
            pass

        @property
        def frames(self) -> None:
            pass

        @property
        def hours(self) -> None:
            pass

        @property
        def minutes(self) -> None:
            pass

        @property
        def seconds(self) -> None:
            pass

    class Song(object):
        def __init__(self, *a, **k):
            """
            This class represents a Live set.
            """
            pass

        @property
        def _live_ptr(self) -> None:
            pass

        @property
        def appointed_device(self) -> None:
            """
            Read, write, and listen access to the appointed Device
            """
            pass

        @property
        def arrangement_overdub(self) -> None:
            """
            Get/Set the global arrangement overdub state.
            """
            pass

        @property
        def back_to_arranger(self) -> None:
            """
            Get/Set if triggering a Clip in the Session, disabled the playback of
Clips in the Arranger.
            """
            pass

        @property
        def can_capture_midi(self) -> None:
            """
            Get whether there currently is material to be captured on any tracks.
            """
            pass

        @property
        def can_jump_to_next_cue(self) -> None:
            """
            Returns true when there is a cue marker right to the playing pos that
we could jump to.
            """
            pass

        @property
        def can_jump_to_prev_cue(self) -> None:
            """
            Returns true when there is a cue marker left to the playing pos that
we could jump to.
            """
            pass

        @property
        def can_redo(self) -> None:
            """
            Returns true if there is an undone action that we can redo.
            """
            pass

        @property
        def can_undo(self) -> None:
            """
            Returns true if there is an action that we can restore.
            """
            pass

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the song.
            """
            pass

        @property
        def clip_trigger_quantization(self) -> None:
            """
            Get/Set access to the quantization settings that are used to fire
Clips in the Session.
            """
            pass

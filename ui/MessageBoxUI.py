import PySimpleGUI as sg

"""
Summary: Show message boxes
"""


class MessageBox_UI(object):
    _warning = "WARNING!"
    _info = "INFO"
    _error = "ERROR"

    # the following methods are different kind of message boxes

    def show_warning_box(self, message):
        sg.popup(self._warning, message, text_color="red", background_color="white", keep_on_top=True)

    def show_error_box(self, message):
        sg.popup(self._error, message, background_color="orange", text_color="red", keep_on_top=True)

    def show_info_box(self, message):
        sg.popup_ok(self._info, message, text_color="black", background_color="white", keep_on_top=True)

    def show_ask_box(self, message):
        sg.popup_ok_cancel(self._info, message, text_color="black", background_color="white", keep_on_top=True)

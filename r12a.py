from kivy.core.window import Keyboard as _Keyboard

_keyboard = _Keyboard() #TODO: hack
keycode_to_string = _keyboard.keycode_to_string

class Keyboard(object):
    keycodes = {
        'w': keycode_to_string(_Keyboard.keycodes['w']),
        's': keycode_to_string(_Keyboard.keycodes['s']),
        'up': keycode_to_string(_Keyboard.keycodes['up']),
        'down': keycode_to_string(_Keyboard.keycodes['down']),
    }

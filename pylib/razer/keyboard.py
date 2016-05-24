"""
Module to handle custom colours
"""

from gi.repository import Gdk
import struct
import subprocess


KEY_MAPPING = {
    # Row 0
    'ESC': (0,1), 'F1' : (0,3), 'F2' : (0,4), 'F3' : (0,5), 'F4' : (0,6), 'F5' : (0,7), 'F6' : (0,8), 'F7' : (0,9), 'F8' : (0,10), 'F9' : (0,11), 'F10' : (0,12), 'F11' : (0,13), 'F12' : (0,14), 'PRTSCR' : (0,15), 'SCRLK' : (0,16), 'PAUSE' : (0,17), 'LOGO' : (0,20), 'JP1': (0, 21),
    # Row 1
    'M1': (1,0), 'BACKTICK': (1,1), '1': (1,2), '2': (1,3), '3': (1,4), '4': (1,5), '5': (1,6), '6': (1,7), '7': (1,8), '8': (1,9), '9': (1,10), '0': (1,11), 'DASH': (1,12), 'EQUALS': (1,13), 'BACKSPACE': (1,14), 'INS': (1,15), 'HOME': (1,16), 'PAGEUP': (1,17), 'NUMLK': (1,18), 'NPFORWARDSLASH': (1,19), 'NPASTERISK': (1,20), 'NPDASH': (1,21),
    # Row 2
    'M2': (2,0), 'TAB': (2,1), 'Q': (2,2), 'W': (2,3), 'E': (2,4), 'R': (2,5), 'T': (2,6), 'Y': (2,7), 'U': (2,8), 'I': (2,9), 'O': (2,10), 'P': (2,11), 'LEFTSQUAREBRACKET': (2,12), 'RIGHTSQUAREBRACKET': (2,13), 'DELETE': (2,15), 'END': (2,16), 'PAGEDOWN': (2,17), 'NP7': (2,18), 'NP8': (2,19), 'NP9': (2,20), 'NPPLUS': (2,21),
    # Row 3
    'M3': (3,0), 'CAPSLK': (3,1), 'A': (3,2), 'S': (3,3), 'D': (3,4), 'F': (3,5), 'G': (3,6), 'H': (3,7), 'J': (3,8), 'K': (3,9), 'L': (3,10), 'SEMICOLON': (3,11), 'APOSTROPHE': (3,12), 'POUNDSIGN': (3,13), 'RETURN': (3,14), 'NP4': (3,18), 'NP5': (3,19), 'NP6': (3,20),
    # Row 4
    'M4': (4,0), 'LEFTSHIFT': (4,1), 'BACKSLASH': (4,2), 'Z': (4,3), 'X': (4,4), 'C': (4,5), 'V': (4,6), 'B': (4,7), 'N': (4,8), 'M': (4,9), 'COMMA': (4,10), 'PERIOD': (4,11), 'FORWARDSLASH': (4,12), 'JP2': (4,13), 'RIGHTSHIFT': (4,14), 'UPARROW': (4,16), 'NP1': (4,18), 'NP2': (4,19), 'NP3': (4,20), 'ENTER': (4,21),
    # Row 5
    'M5': (5,0), 'LEFTCTRL': (5,1), 'SUPER': (5,2), 'LEFTALT': (5,3), 'SPACE': (5,7), 'RIGHTALT': (5,11), 'FN': (5,12), 'CTXMENU': (5,13), 'RIGHTCTRL': (5,14), 'LEFTARROW': (5,15), 'DOWNARROW': (5,16), 'RIGHTARROW': (5,17), 'NP0': (5,19), 'NPPERIOD': (5,20)
}

#
EVENT_MAPPING = {
    1: 'ESC', 2: '1',  3: '2',  4: '3',  5: '4',  6: '5',  7: '6',  8: '7',  9: '8',
    10: '9', 11: '0', 12: 'DASH', 13: 'EQUALS', 14: 'BACKSPACE', 15: 'TAB', 16: 'Q', 17: 'W', 18: 'E', 19: 'R',
    20: 'T', 21: 'Y', 22: 'U', 23: 'I', 24: 'O', 25: 'P', 26: 'LEFTSQUAREBRACKET', 27: 'RIGHTSQUAREBRACKET', 28: 'RETURN', 29: 'LEFTCTRL',
    30: 'A', 31: 'S', 32: 'D', 33: 'F', 34: 'G', 35: 'H', 36: 'J', 37: 'K', 38: 'L', 39: 'SEMICOLON',
    40: 'APOSTROPHE', 41: 'BACKTICK', 42: 'LEFTSHIFT', 43: 'POUNDSIGN', 44: 'Z', 45: 'X', 46: 'C', 47: 'V', 48: 'B', 49: 'N',
    50: 'M', 51: 'COMMA', 52: 'PERIOD', 53: 'FORWARDSLASH', 54: 'RIGHTSHIFT', 55: 'NPASTERISK', 56: 'LEFTALT', 57: 'SPACE',
    58: 'CAPSLK', 59: 'F1',
    60: 'F2', 61: 'F3', 62: 'F4', 63: 'F5', 64: 'F6', 65: 'F7', 66: 'F8', 67: 'F9', 68: 'F10', 69: 'NUMLK',
    70: 'SCRLK', 71: 'NP7', 72: 'NP8', 73: 'NP9', 74: 'NPDASH', 75: 'NP4', 76: 'NP5', 77: 'NP6', 78: 'NPPLUS', 79: 'NP1',
    80: 'NP2', 81: 'NP3', 82: 'NP0', 83: 'NPPERIOD', 86: 'BACKSLASH', 87: 'F11', 88: 'F12',
    96: 'ENTER', 97: 'RIGHTCTRL', 98: 'NPFORWARDSLASH', 99: 'PRTSCR',
    100: 'RIGHTALT', 102: 'HOME', 103: 'UPARROW', 104: 'PAGEUP', 105: 'LEFTARROW', 106: 'RIGHTARROW', 107: 'END', 108: 'DOWNARROW', 109: 'PAGEDOWN', 110: 'INS',
    111: 'DELETE', 119: 'PAUSE',
    125: 'SUPER', 127: 'CTXMENU',
    183: 'M1', 184: 'M2', 185: 'M3', 186: 'M4', 187: 'M5',
    194: 'FN',
}

XTE_MAPPING = {
    'ESC': 'Escape',
    'DASH': '-',
    'EQUALS': '=',
    'BACKSPACE': 'BackSpace',
    'TAB': 'Tab',
    'LEFTSQUAREBRACKET': ']',
    'RIGHTSQUAREBRACKET': '[',
    'RETURN': 'Return',
    'LEFTCTRL': 'Control_L',
    'SEMICOLON': ':',
    'APOSTROPHE': '\'',
    'BACKTICK': '`',
    'LEFTSHIFT': 'Shift_L',
    'POUNDSIGN': '#',
    'COMMA': ',',
    'PERIOD': '.',
    'FORWARDSLASH': '/',
    'RIGHTSHIFT': 'Shift_R',
    'NPASTERISK': '*',
    'LEFTALT': 'Alt_L',
    'SPACE': '" "',
    'CAPSLK': None,
    'NUMLK': None,
    'SCRLK': None,
    'NP7': '7',
    'NP8': '8',
    'NP9': '9',
    'NPDASH': '-',
    'NP4': '4',
    'NP5': '5',
    'NP6': '6',
    'NPPLUS': '+',
    'NP1': '1',
    'NP2': '2',
    'NP3': '3',
    'NP0': '0',
    'NPPERIOD': '.',
    'BACKSLASH': '\\',
    'ENTER': 'Enter',
    'RIGHTCTRL': 'Control_r',
    'NPFORWARDSLASH': '/',
    'RIGHTALT': 'Alt_R',
    'HOME': 'Home',
    'UPARROW': None,
    'PAGEUP': 'Page_Up',
    'LEFTARROW': None,
    'RIGHTARROW': None,
    'END': 'End',
    'DOWNARROW': None,
    'PAGEDOWN': 'Page_Down',
    'INS': 'Insert',
    'DELETE': 'Delete',
    'PAUSE': None,
    'SUPER': 'Meta_L',
    'CTXMENU': None,
    'M1': None,
    'M2': None,
    'M3': None,
    'M4': None,
    'M5': None,
    'FN': None,
}

class KeyDoesNotExistError(Exception):
    """
    Simple custom error
    """
    pass

class NoBackupError(Exception):
    pass

class RGB(object):

    @staticmethod
    def clamp(value):
        """
        Clamp a value to 0-255

        :param value: Value to be clamped
        :type value: integer or float

        :return: Integer in the range of 0-255
        :rtype: int
        """
        result = int(value)

        if value > 255:
            result = 255
        elif value < 0:
            result = 0

        return result

    def __init__(self, red=0, green=0, blue=0):
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        """
        Getter for red element

        :return: Red element
        :rtype: int
        """
        return self._red

    @red.setter
    def red(self, value):
        """
        Setter for red value

        :param value: Red value
        :type value: int or float
        """
        self._red = RGB.clamp(value)

    @property
    def green(self):
        """
        Getter for green element

        :return: Green element
        :rtype: int
        """
        return self._green

    @green.setter
    def green(self, value):
        """
        Setter for green value

        :param value: Green value
        :type value: int or float
        """
        self._green = RGB.clamp(value)

    @property
    def blue(self):
        """
        Getter for blue element

        :return: Blue element
        :rtype: int
        """
        return self._blue

    @blue.setter
    def blue(self, value):
        """
        Setter for blue value

        :param value: Blue value
        :type value: int or float
        """
        self._blue = RGB.clamp(value)

    def set(self, colour_tuple):
        """
        Sets all the colours at once

        :param colour_tuple: Tuple of R,G,B elements
        :type colour_tuple: tuple
        """
        # Shortcut to clamp all parameters and assign to the 3 variables
        self._red, self._green, self._blue = list(map(RGB.clamp, colour_tuple))

    def get(self):
        """
        Gets all the colours as a tuple

        :return: RGB tuple
        :rtype: tuple
        """
        return self._red, self._green, self._blue

    def __bytes__(self):
        """
        Convert to bytes

        :return: Byte string
        :rtype: bytearray
        """
        return bytes((self._red, self._green, self._blue))

    def __repr__(self):
        """
        String representation

        :return: String
        :rtype: str
        """
        return "RGB Object (#{0:02X}{1:02X}{2:02X})".format(self._red, self._green, self._blue)

class KeyboardColour(object):
    """
    Keyboard class which represents the colour state of the keyboard.
    """

    @staticmethod
    def gdk_colour_to_rgb(gdk_color):
        """
        Converts GDK colour to (R,G,B) tuple

        :param gdk_color: GDK colour
        :type gdk_color: Gdk.Color or tuple

        :return: Tuple of 3 ints
        :rtype: tuple
        """
        if isinstance(gdk_color, (list, tuple)):
            return gdk_color

        assert type(gdk_color) is Gdk.Color, "Is not of type Gdk.Color"

        red = int(gdk_color.red_float * 255)
        green = int(gdk_color.green_float * 255)
        blue = int(gdk_color.blue_float * 255)

        return red, green, blue

    def __init__(self):
        self.rows = []

        self.backup = None

        self.reset_rows()

    def backup_configuration(self):
        """
        Backs up the current configuration
        """
        self.backup = KeyboardColour()
        self.backup.get_from_total_binary(self.get_total_binary())

    def restore_configuration(self):
        """
        Restores the previous configuration
        """
        if self.backup is None:
            raise NoBackupError()

        self.rows = self.backup.rows
        self.backup = None

    def get_rows_raw(self):
        """
        Gets the raw representation of the rows

        :return: Rows
        :rtype: list
        """
        return self.rows

    def reset_rows(self):
        """
        Reset the rows of the keyboard
        """
        self.rows.clear()

        for row in range(0, 6):
            # Create 22 rgb values
            self.rows.append([RGB() for _ in range(0,22)])

    def set_key_colour(self, row, col, colour):
        """
        Set the colour of a key

        :param row: Row ID
        :type row: int

        :param col: Column ID
        :type col: int

        :param colour: Colour to set
        :type colour: Gdk.Color or tuple

        :raises KeyDoesNotExistError: If given key does not exist
        """
        self.rows[row][col].set(KeyboardColour.gdk_colour_to_rgb(colour))

    def get_key_colour(self, key):
        """
        Get the colour of a key

        :param key: Key to set the colour of
        :type key: str

        :raises KeyDoesNotExistError: If given key does not exist
        """
        if key not in KEY_MAPPING:
            raise KeyDoesNotExistError("The key \"{0}\" does not exist".format(key))

        row_id, col_id = KEY_MAPPING[key]
        return self.rows[row_id][col_id].get()

    def reset_key(self, row, col):
        """
        Reset the colour of a key

        :param row: Row ID
        :type row: int

        :param col: Column ID
        :type col: int

        :raises KeyDoesNotExistError: If given key does not exist
        """
        self.rows[row][col].set((0, 0, 0))

    def get_row_binary(self, row_id):
        """
        Gets the binary payload for a given row

        :param row_id: Row ID
        :type row_id: int

        :return: Byte string of 67 bytes, Row ID byte then 22 RGB bytes
        :rtype: bytearray
        """
        assert isinstance(row_id, int), "Row ID is not an int"
        payload = bytes([row_id])

        for rgb in self.rows[row_id]:
            payload += bytes(rgb)

        return payload

    def get_total_binary(self):
        """
        Gets the binary payload for the whole keyboard

        :return: Byte string of 6*67 bytes, (Row ID byte then 22 RGB bytes) * 6
        :rtype: bytearray
        """
        payload = b''

        for row in range(0,6):
            payload += self.get_row_binary(row)

        return payload

    def get_from_total_binary(self, binary_blob):
        """
        Load in a binary blob which is the output from get_total_binary

        :param binary_blob: Binary blob
        :type binary_blob: bytearray
        """
        self.reset_rows()

        for row_id in range (0, 6):
            binary_blob = binary_blob[1:] # Skip first byte

            for col_id, binary_rgb in enumerate([binary_blob[i:i+3] for i in range(0, 66, 3)]):
                rgb = struct.unpack('=BBB', binary_rgb)
                self.rows[row_id][col_id].set(rgb)

            binary_blob = binary_blob[66:] # Skip the current row


def get_keyboard_layout():
    """
    Function to get the keyboard layout

    I can see this becoming an ugly mess as it'll need to support multiple keyboard layouts which have different names
    on different systems

    :return: Keyboard layout
    :rtype: str
    """
    cmd = ['setxkbmap', '-query']
    output = subprocess.check_output(cmd)

    result = 'gb'

    if output:
        output = output.decode('utf-8').splitlines()
        layout = 'gb'
        variant = ''
        for line in output:
            if line.startswith('layout'):
                layout = line.split(':', 1)[1].strip()
                if layout.find(',') > -1:
                    layout = layout.split(',')[0]

            elif line.startswith('variant'):
                variant = line.split(':', 1)[1].strip().split(',')[0]

                if 'latin9' in variant: # Removes some rubbish from ubuntu
                    variant = 'latin9'

        if variant == '':
            result = layout
        else:
            result = layout + '-' + variant

    # If the user has an international layout variant ignore that part
    result = result.replace('-altgr-intl', '')

    return result
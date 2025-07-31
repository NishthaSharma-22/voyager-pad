import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.OLED import OLED

keyboard = KMKKeyboard()
macros = Macros()
oled = OLED(
    oled_addr = 0x3C,
    to_display="floating in space on a piece of rock",
    i2c_sda = board.GP5,
    i2c_scl= board.GP6,
)

keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(macros)
keyboard.extensions.append(oled)



PINS = [board.GP1, board.GP2, board.GP3, board.GP4, board.GP7, board.GP8, board.GP9]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False,
)

keyboard.keymap = [
    [
    KC.MACRO(Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT)),
    KC.BRIGHTNESS_DOWN,
    KC.BRIGHTNESS_UP,
    KC.VOLU,
    KC.VOLD,
    KC.MUTE,
    KC.MEDIA_NEXT_TRACK,
    ]
]

if __name__=="__main__":
    keyboard.go()



# FKEYS WITH HOTKEYS

## Installation
```
git clone https://github.com/iliS10/fkeys-hotkeys.git
```
```
cd fkeys-hotkeys
```
```
pip install pynput
pip install pystray
pip install pillow
```
For __execute the script__ you can directly __click on the main.pyw__

And __press "Exit"__ in your taskbar __to close it__

## Set FKEYS at hotkeys with num and caps lock

To press fkeys use __capslock+1 capslock+2 capslock+3__ etc...
                          for __F1 F2 F3__ etc...
                          
You can press __Alt__ with this combo of keys to press something like __alt + capslock + 4__ that return __alt+f4__

### The script is set for azerty keyboards, __to configure it for qwerty keyboard change main.pyw
__to set__
```
key_mapping = {
    '&': keyboard.Key.f1,
    'é': keyboard.Key.f2,
    '"': keyboard.Key.f3,
    '\'': keyboard.Key.f4,
    '(': keyboard.Key.f5,
    '-': keyboard.Key.f6,
    'è': keyboard.Key.f7,
    '_': keyboard.Key.f8,
    'ç': keyboard.Key.f9,
    'à': keyboard.Key.f10,
    ')': keyboard.Key.f11,
    '=': keyboard.Key.f12,
}
```
__with__
```
key_mapping = {
    '1': keyboard.Key.f1,
    '2': keyboard.Key.f2,
    '3': keyboard.Key.f3,
    '4'': keyboard.Key.f4,
    '5': keyboard.Key.f5,
    '6': keyboard.Key.f6,
    '7': keyboard.Key.f7,
    '8': keyboard.Key.f8,
    '9': keyboard.Key.f9,
    '(': keyboard.Key.f10,
    ')': keyboard.Key.f11,
    '-': keyboard.Key.f12,
}
```
or other keys

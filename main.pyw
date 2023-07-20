from pynput import keyboard
from pystray import MenuItem as Item
from PIL import Image
import pystray
import threading
import sys
import os
import ctypes

# Mapping of the keys from AZERTY keyboard to the function keys
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

# Global state
state = {
    "caps_lock": False,
    "alt": False
}

# Dictionary to store the state of each key combination
key_states = {}

# Create a Controller instance to control the keyboard
controller = keyboard.Controller()

# Load the necessary functions from ctypes
user32 = ctypes.windll.user32
GetKeyState = user32.GetKeyState
CAPS_LOCK_KEY = 0x14

def is_caps_lock_on():
    """
    Check if Caps Lock is on using ctypes.
    """
    return GetKeyState(CAPS_LOCK_KEY) & 1

def execute_combination(key_combination):
    for key in key_combination:
        controller.press(key)
        controller.release(key)

def on_press(key):
    global key_states

    # Check if caps lock is pressed
    if key == keyboard.Key.caps_lock:
        state["caps_lock"] = True

    # Check if alt is pressed
    if key == keyboard.Key.alt:
        state["alt"] = True

    # If caps lock is pressed, check the mapping
    if state["caps_lock"]:
        for k, v in key_mapping.items():
            if key == keyboard.KeyCode.from_char(k):
                if state["alt"]:
                    execute_combination([keyboard.Key.alt, v])
                else:
                    execute_combination([v])

                # Press Caps Lock again if it's still active after the combination
                if is_caps_lock_on():
                    controller.press(keyboard.Key.caps_lock)
                    controller.release(keyboard.Key.caps_lock)

                # Update the key combination state
                key_states[k] = True

def on_release(key):
    global key_states

    # Check if caps lock is released
    if key == keyboard.Key.caps_lock:
        state["caps_lock"] = False

    # Check if alt is released
    if key == keyboard.Key.alt:
        state["alt"] = False

    # Check if any key combination state needs to be reset
    for k in key_mapping.keys():
        if key == keyboard.KeyCode.from_char(k):
            key_states[k] = False

# Start a listener in a different thread
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Create an icon
icon = pystray.Icon(
    "name",
    Image.open("icon.png"),  # replace "icon.png" with the path to your icon
    "My System Tray Icon",
    menu=pystray.Menu(Item('Quit', lambda icon, item: os._exit(0)))
)

# Run the icon
icon.run()

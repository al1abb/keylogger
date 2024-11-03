def get_pressed_keys_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        result = []
        
        for line in lines:
            # Check for space key
            if "Special key Key.space pressed" in line:
                result.append(" ")
            # Check for normal key presses
            elif "Key" in line and "pressed" in line:
                parts = line.split("Key ")
                if len(parts) > 1:
                    key_info = parts[1].split(" pressed")
                    if len(key_info) > 0:
                        key_char = key_info[0]
                        result.append(key_char)

        return ''.join(result)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Prompt the user for the relative path to the key_log.txt file
file_path = input("Please enter the relative path to the key_log.txt file (e.g., dist/key_log.txt): ")

# Process the file and display the output
output = get_pressed_keys_from_file(file_path)
if output is not None:
    print("Output:\n")
    print(output)

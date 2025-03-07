import os

def get_path():
    file_name = "Persian-WikiText.txt"
    # Walk through all directories and subdirectories starting from the root
    for root, dirs, files in os.walk('/'):  # You can replace '/' with a specific path if needed
        if file_name in files:
            return os.path.join(root, file_name)  # Returns the absolute path of the file
    return "File not found."



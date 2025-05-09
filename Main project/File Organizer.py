import os


def organize_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through all files in the folder
    for file in files:
        file_path = os.path.join(folder_path, file)
    # print(file_path)
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_name, file_extension = os.path.splitext(file)

        # If no extension (hidden files), skip
        if file_extension == '':
            continue

        # Remove the dot from the extension and make it uppercase for folder name
        file_extension = file_extension[1:].upper()

        # Create a subfolder for the extension if it doesn't exist
        subfolder_path = os.path.join(folder_path, file_extension)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        # Move the file to the corresponding subfolder
        new_file_path = os.path.join(subfolder_path, file)
        os.rename(file_path, new_file_path)
        print(f"Moved: {file} -> {file_extension}")


# Ask the user to input the folder path
folder_path = input("Enter the path of the folder to organize: ")

# Check if the folder exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    organize_files(folder_path)
else:
    print("Invalid folder path!")




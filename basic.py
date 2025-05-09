import os
print(os.getcwd())  # Current working directory
print(os.listdir())             # List current directory
print(os.listdir('f:/Python/Python'))  # List a specific path
# os.mkdir('my_dir')
# os.mkdir('test_dir')           # Create one directory
# os.makedirs('a/b/c')           # Create nested directories
# os.rmdir('my_dir')           # Remove one directory (must be empty)
# os.removedirs('a/b/c')         # Removes nested empty dirs if all file empty its delete all file
# os.rmdir('a/b/c')  # Only removes 'c' if it's empty

# os.rename('old.txt', 'new.txt')  # Rename file
# os.remove('file.txt')           # Delete file

print(os.path.exists('new.txt'))  # True/False
print(os.path.exists('my_dir'))  # True/False

print(os.path.isdir('my_dir'))  # Check if it's a director
print(os.path.isfile('new.txt'))  # Check if it's a director

path = os.path.join("folder", "subfolder", "file.txt")
print(path)

cwd = os.getcwd()
file_path = os.path.join(cwd, "data", "log.txt")

print(file_path)

dir_path = os.path.join("projects", "python", "output")
# creates the whole path if it doesn't exist
os.makedirs(dir_path, exist_ok=True)

file_path = os.path.join(dir_path, "result.txt")

print(file_path)

with open(file_path, "w") as f:
    f.write("Task completed.")


file_path = "log.txt"

with open(file_path, "a") as f:
    f.write("Appended line.\n")

with open(file_path, "r") as f:
    content = f.read()
    print(content)

stats = os.stat('log.txt')
print(stats.st_size)  # File size in bytes
print(stats.st_mtime)  # Last modified time (timestamp)

main = r"F:\Python\Python\OS\os_walk"
print(main)

print(list(os.walk(main)))

for root, dirs, files in os.walk(main):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
    print("-" * 40)

os.system('echo Hello')  # Run terminal command

os.environ['MY_VAR'] = '123'          # Set a new environment variable
# This does not set the variable permanently on your system. api
print(os.getenv('MY_VAR'))

print(os.getcwd())
# Change current directory to 'some/folder'
# os.chdir('os_walk/Folder02/Folder03')

# print(os.getcwd())

print(os.cpu_count())  # Number of logical CPUs

# os.remove('log.txt')

# os.replace("new.txt", "final.txt")  # safely replace

# os.rename("log.txt", "backup/data.txt") canbe rename and replace src to dest

path = "folder/file.txt"

print(os.path.abspath(path))        # 🔹 Full absolute path
print(os.path.basename(path))       # 🔹 Just the file name
print(os.path.dirname(path))        # 🔹 Just the directory part
print(os.path.splitext(path)) 
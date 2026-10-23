# module ex5
import os

"""
creates the directory structure for
a new project:
• a root folder named after the project,
• a subfolder src/ for the source code,
• a subfolder docs/ for the documentation,
• a file README.md in the root folder, and
• a file main.py in the folder src/.

If the project folder already exists, the function
prints a message saying so. Directories must be
created recursively, and both README.md and main.py
get some placeholder content.
"""

def create_project_structure(base_path, project_name="new_folder"):
    path = base_path.append(project_name)

    os.mkdir(path)
    return None

"""
A function that uses os.walk() to recursively traverse
the directory structure starting at path and prints every
file and folder. The output must clearly distinguish between
files and directories.
"""
def traverse_directory(path):
    return None

"""
• prints the file size, the time of the last modification, and the creation
time (the latter is platform-dependent), and
• makes the file read-only and then writable again.

Use os.stat() to retrieve the metadata and os.chmod() to change the per-
missions.
"""
def file_metadata(file_path):
    return None

"""
Uses os.walk() to search the given directory and its
subdirectories for all files with the given extension
(e.g., .py or .md). The function returns a list of the
full paths of all files found.
"""
def find_files_by_extension(path, extension):
    return None

"""

"""
def delete_files_and_directories(path):
    return None

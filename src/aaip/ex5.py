# module ex5
import os, stat, time

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
    path = os.path.join(base_path, project_name)
    if os.path.exists(path):
        print(f"Project directory already exists: {path}")
        return None

    src_path = os.path.join(path, "src")
    os.makedirs(src_path)
    os.makedirs(os.path.join(path, "docs"))

    with open(os.path.join(path, "README.md"), 'w') as fp:
        fp.write(f"## README for {project_name}. \n")

    with open(os.path.join(src_path, "main.py"), 'w') as fp:
        fp.write('print("Hello World!")\n')

    return None

"""
A function that uses os.walk() to recursively traverse
the directory structure starting at path and prints every
file and folder. The output must clearly distinguish between
files and directories.
"""
def traverse_directory(path):
    
    for (root, dirs, files) in os.walk(path):
        for dir_name in dirs:
            print("[DIR]  %s" % os.path.join(root, dir_name))
        for file in files:
            print("[FILE] %s" % os.path.join(root, file))
    return None

"""
Syntax: os.stat(path)  

Parameter: path: A string or bytes object representing a valid path   

Return Type: This method returns a 'stat_result' object of class 'os.stat_result' which represents the status of specified path. The returned 'stat-result' object has following attributes: 

    st_mode: It represents file type and file mode bits (permissions).
    st_ino: It represents the inode number on Unix and the file index on Windows platform.
    st_dev: It represents the identifier of the device on which this file resides.
    st_nlink: It represents the number of hard links.
    st_uid: It represents the user identifier of the file owner.
    st_gid: It represents the group identifier of the file owner.
    st_size: It represents the size of the file in bytes.
    st_atime: It represents the time of most recent access. It is expressed in seconds.
    st_mtime: It represents the time of most recent content modification. It is expressed in seconds.
    st_ctime: It represents the time of most recent metadata change on Unix and creation time on Windows. It is expressed in seconds.
    st_atime_ns: It is same as st_atime but the time is expressed in nanoseconds as an integer.
    st_mtime_ns: It is same as st_mtime but the time is expressed in nanoseconds as an integer.
    st_ctime_ns: It is same as st_ctime but the time is expressed in nanoseconds as an integer.
    st_blocks: It represents the number of 512-byte blocks allocated for file.
    st_rdev: It represents the type of device, if an inode device.
    st_flags: It represents the user defined flags for file.
"""

"""
• prints the file size, the time of the last modification, and the creation
time (the latter is platform-dependent), and
• makes the file read-only and then writable again.

Use os.stat() to retrieve the metadata and os.chmod() to change the per-
missions.
"""
def file_metadata(file_path):

    stat_result = os.stat(file_path)
    print(f"File size: {stat_result.st_size} Bytes")
    print(f"Time of last modification: {time.ctime(stat_result.st_mtime)}")
    # st_birthtime is not available everywhere; st_ctime is creation time only on Windows
    created = getattr(stat_result, "st_birthtime", stat_result.st_ctime)
    print(f"Time of creation (platform-dependent): {time.ctime(created)}")

    original_mode = stat.S_IMODE(stat_result.st_mode)

    os.chmod(file_path, stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
    print("Read only mode activated")

    os.chmod(file_path, original_mode | stat.S_IWRITE)
    print("Writable mode activated")

    return None

"""
Uses os.walk() to search the given directory and its
subdirectories for all files with the given extension
(e.g., .py or .md). The function returns a list of the
full paths of all files found.
"""
def find_files_by_extension(path, extension):
    
    matches = []
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if file.lower().endswith(extension.lower()):
                matches.append(os.path.join(root, file))

    return matches

"""
Write a function delete_files_and_directories(path)
that deletes all files in the directory, then all of its
subdirectories, and finally the directory itself.
The function must handle nested directories and files.
Use os.remove() for files and os.rmdir() for
directories (note that os.rmdir() only removes empty directories).
"""
def delete_files_and_directories(path):
    
    for (root, dirs, files) in os.walk(path, topdown= False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if os.path.islink(dir_path):
                os.remove(dir_path)
            else:
                os.rmdir(dir_path)

    os.rmdir(path)

    return None

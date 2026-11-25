# module ex7
import os
import shutil
import argparse

"""
Write a more advanced
command-line tool for file management using the argparse module. The tool
copies, moves, and renames files, and it provides detailed help and error messages
through argparse.
Requirements:
• The tool supports the following subcommands:
– copy: copy a file from the source to the destination,
– move: move a file from the source to the destination, and
– rename: rename a file.
• Source and destination are passed with the arguments –src and –dst; the
order of the arguments does not matter.
• copy accepts one or more destinations and copies the file to each of them.
• Missing arguments lead to clear error messages, and -h or –help shows a
detailed help.
• Each operation prints a confirmation message, such as File copied
successfully.
• For the file operations, you may use the shutil module.
• An example usage is shown in Listing 2
"""

def main():
    parser = argparse.ArgumentParser(description="Copy, move and rename files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    copy_parser = subparsers.add_parser("copy", help="copy a file to one or more destinations")
    copy_parser.add_argument("--src", required=True, help="source file")
    copy_parser.add_argument("--dst", required=True, nargs="+", help="one or more destinations")

    move_parser = subparsers.add_parser("move", help="move a file")
    move_parser.add_argument("--src", required=True, help="source file")
    move_parser.add_argument("--dst", required=True, help="destination")

    rename_parser = subparsers.add_parser("rename", help="rename a file")
    rename_parser.add_argument("--src", required=True, help="current file name")
    rename_parser.add_argument("--dst", required=True, help="new file name")

    args = parser.parse_args()

    try:
        if args.command == "copy":
            for dst in args.dst:
                shutil.copy(args.src, dst)
            print("File copied successfully")
        elif args.command == "move":
            shutil.move(args.src, args.dst)
            print("File moved successfully")
        else:
            os.rename(args.src, args.dst)
            print("File renamed successfully")
    except FileNotFoundError:
        parser.error(f"File not found: {args.src}")

if __name__ == "__main__":
    main()

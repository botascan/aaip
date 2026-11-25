# module ex6
import re
import sys
"""
Write a Python script that acts as a
command-line tool for basic text file manipulation: counting words, counting lines,
and searching for a word in a file. Use the sys module to read the command-line
arguments.

Requirements:

• The script takes the following arguments:
– the file name,
– the operation to perform: count_words, count_lines, or search_word, and
– for search_word only, the word to search for.
• Depending on the operation, the script
– prints the number of words in the file (count_words),
– prints the number of lines in the file (count_lines), or
– prints all lines that contain the given word (search_word).
• The script handles a missing file and invalid arguments gracefully.
• An example usage is shown in Listing 1.
"""

def main():
    if len(sys.argv) < 3:
        print("Usage: ex6.py <file> count_words|count_lines|search_word [word]")
        return 1

    file_path = sys.argv[1]
    op_name = sys.argv[2]

    try:
        if op_name == "count_words":
            print(count_words(file_path))
        elif op_name == "count_lines":
            print(count_lines(file_path))
        elif op_name == "search_word" and len(sys.argv) == 4:
            for line in search_word(file_path, sys.argv[3]):
                print(line)
        else:
            print("Invalid arguments")
            return 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 1

    return 0

def count_words(file_path) -> int:
    with open(file_path, encoding="utf-8") as fp: # encoding utf-8 to get normal characters OS-independent
        return sum(len(line.split()) for line in fp)

def count_lines(file_path) -> int:
    with open(file_path, encoding="utf-8") as fp:
        return sum(1 for _ in fp)

def search_word(file_path, word_to_search) -> list:
    # whole-word, case-sensitive match
    pattern = rf"\b{re.escape(word_to_search)}\b"
    with open(file_path, encoding="utf-8") as fp:
        return [line.rstrip("\n") for line in fp if re.search(pattern, line)]

if __name__ == "__main__":
    sys.exit(main())

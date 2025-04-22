from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    char_count = get_num_chars(get_book_text(path))
    num_words = get_num_words(get_book_text(path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
from stats import *

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    char_count = get_num_chars(get_book_text("books/frankenstein.txt"))
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(char_count)

main()
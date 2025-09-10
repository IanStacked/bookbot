from stats import find_len_string
from stats import find_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_chars = find_num_char(text)
    num_words = find_len_string(text)
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
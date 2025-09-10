from stats import find_len_string
from stats import find_num_char
from stats import sort_dic
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_chars = find_num_char(text)
    num_words = find_len_string(text)
    sorted_dic = sort_dic(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for tuple in sorted_dic:
        if(tuple[0].isalpha()):
            print(f"{tuple[0]}: {tuple[1]}")
    sys.exit(0)
    

main()
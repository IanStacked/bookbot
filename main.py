from stats import find_len_string
from stats import find_num_char
from stats import sort_dic

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_chars = find_num_char(text)
    num_words = find_len_string(text)
    sorted_dic = sort_dic(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for tuple in sorted_dic:
        if(tuple[0].isalpha()):
            print(f"{tuple[0]}: {tuple[1]}")
            
main()
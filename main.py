def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def find_len_string(string):
        return len(string.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    len = find_len_string(text)
    print(f"{len} words found in the document")

main()
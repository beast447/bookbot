from stats import count_words
from stats import count_chars
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    num_chars = count_chars(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    print(f"{num_chars}")
    

main()

from stats import count_words
from stats import count_chars
from stats import sort_on
from stats import sort_dict

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    num_chars = count_chars(get_book_text("books/frankenstein.txt"))
    sorted_dict = sort_dict(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for item in sorted_dict:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END =============")
main()

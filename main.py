from stats import count_words, count_chars, sort_on, sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num_words = count_words(get_book_text(sys.argv[1]))
        num_chars = count_chars(get_book_text(sys.argv[1]))
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

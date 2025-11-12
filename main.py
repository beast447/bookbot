def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    split_string = text.split()
    word_count = len(split_string)
    return word_count

def main():
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()

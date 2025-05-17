from stats import word_count
from stats import character_count
from stats import sorted_dictionaries
import sys

def get_book_text (book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for character in sorted_dictionaries(character_count(book_text)):
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    

main()
from stats import word_count
from stats import character_count
from stats import sorted_dictionaries

def get_book_text (book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(frankenstein)} total words")
    print("--------- Character Count -------")
    for character in sorted_dictionaries(character_count(frankenstein)):
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    

main()
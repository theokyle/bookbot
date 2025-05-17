from stats import word_count
from stats import character_count

def get_book_text (book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(f"{word_count(frankenstein)} words found in the document")
    print(character_count(frankenstein))

main()
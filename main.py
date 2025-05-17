def get_book_text (book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
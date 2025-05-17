def get_book_text (book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents
    
def word_count (string):
    return len(string.split())

def main():
    print(f"{word_count(get_book_text("books/frankenstein.txt"))} words found in the document")

main()
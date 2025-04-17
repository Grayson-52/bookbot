def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text
    
def main():
    filepath = ("books/frankenstein.txt")
    book = get_book_text(filepath)
    print(book)

main()

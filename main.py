from stats import get_book_text
from stats import word_counter

def main():
    filepath = ("books/frankenstein.txt")
    book = word_counter(filepath)
    print(f"{book} words found in the document")

main()

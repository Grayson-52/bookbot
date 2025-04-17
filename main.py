def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def word_counter(filepath):
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        count = len(words)
    return count

def main():
    filepath = ("books/frankenstein.txt")
    book = word_counter(filepath)
    print(f"{book} words found in the document")

main()

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

def character_count(filepath):
    dict = {}
    with open(filepath) as f:
        text = f.lower()

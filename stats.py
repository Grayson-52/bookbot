from collections import Counter

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
    characters = {}
    with open(filepath) as f:
        book = f.read().lower()
        chars = [x for x in book]
        for character in chars:
            if character not in characters:
                characters[character] = 0
            characters[character] += 1
    return characters

def sort_count(characters):
    chars = []
    for char, count in characters.items():
        if char.isalpha():
            char_info = {"char": char, "count": count}
            chars.append(char_info)
    def sort_on(dict):
        return dict["count"]
    chars.sort(reverse=True, key=sort_on)
    return chars
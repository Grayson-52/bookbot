from collections import Counter
import sys
from stats import get_book_text
from stats import word_counter
from stats import character_count
from stats import sort_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = (sys.argv[1])
    word_count = word_counter(filepath)
    characters = character_count(filepath)
    report = sort_count(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in report:
        # 'char' is the key while 'count' is the amount
        print(f"{char['char']}: {char['count']}")
    print("============= END ===============")

main()

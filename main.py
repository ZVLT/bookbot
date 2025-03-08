import sys
from stats import number_of_words
from stats import number_of_letters
from stats import sorted_letters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def letter_report_order(letters_list):
    for l in letters_list:
        print(f"{list(l)[0]}: {list(l.values())[0]}")

def path_input(arg):
    if len(arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return arg[1]

def main():
    path_to_file = path_input(sys.argv)
    book = get_book_text(path_to_file)
    num_words = number_of_words(book)
    num_letters = number_of_letters(book)
    sorted = sorted_letters(num_letters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    letter_report_order(sorted)
    print("============= END ===============")

main()
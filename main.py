from stats import get_num_words, sort_letters_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def print_report(book, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item['letter'].isalpha():
            print(f"{item['letter']}: {item['num']}")
    print("============= END ===============")
          
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]

    file_contents = get_book_text(book)
    num_words, letters = get_num_words(file_contents)
    sorted_list = sort_letters_list(letters)
    print_report(book, num_words, sorted_list)
    #print(f"{num_words} words found in the document")
    #print(letters)

main()
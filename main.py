from stats import count_words, count_char_in_string, print_report, sort_dict
import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path_to_book = sys.argv[1]

    with open(path_to_book) as f:
        file_content = f.read()

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {count_words(file_content)} total words")
    print('--------- Character Count -------')
    for key, val in sort_dict(count_char_in_string(file_content)).items():
        print(f"'{key}: {val}'")
    print('============= END ===============')

main()

from stats import word_count, char_count, dict_to_list
import sys

def sort_on(item):
    return item["num"]

# Get_book_text takes a file path and returns a string with the contents of the file
def get_book_text(filepath):
    file_contents = filepath.read()
    return file_contents

def report(file_location_g, book, c_list):

    print(
    f" ============ BOOKBOT ============\n", 
    f"Analyzing book found at {file_location_g}...\n\n",
    f"----------- Word Count ----------\n",
    f"Found {word_count(book)} total words\n\n",
    f"-------- Character Count --------",
    )
    for char in range(len(c_list)):
        if c_list[char]['char'].isalpha():
            print (f"{c_list[char]['char']}: {c_list[char]['num']}")

# main function opens a file and uses the get_book_text function in order to return a string
# that contains the contents of the file
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]        
        with open(file_location) as f:
            new_book = get_book_text(f)
            char_dict = char_count(new_book)
            char_list = dict_to_list(char_dict)
            char_list.sort(reverse=True, key= sort_on)
            report(file_location, new_book, char_list)

main()




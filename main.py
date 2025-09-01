from stats import get_num_words, read_file,count_letters
from sys import argv, path


def main():
    if len(argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    mypath =path[0]+"/"+argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {mypath}...")
    input = read_file(mypath)
    no_of_words = get_num_words(input)
    print("----------- Word Count ----------")
    print(f"Found {no_of_words} total words\n")
    print("---------Character Count---------")
    count_letters(input)
    print("============= END ===============")








main()

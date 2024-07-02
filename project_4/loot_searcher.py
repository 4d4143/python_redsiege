from pathlib import Path
import sys
import argparse

def load_wordlist(wordlist_input_file):
    wordlist = []

    with open(wordlist_input_file, 'r') as wordlist_input:
        file_lines = wordlist_input.readlines()
        for line in file_lines:
            wordlist.append(line.strip())

    return wordlist

def check_directory_property(input_directory):
    if Path(input_directory).exists() and Path(input_directory).is_dir:
        return True
    else:
        return False

def get_filepaths(input_directory):
    if check_directory_property(input_directory) == True:
        filepaths_list = [path for path in Path(input_directory).glob('**/*') if path.is_file]
    else:
        sys.exit(1)

    return filepaths_list

def search_filenames(filepaths, filename_search_list):
    matched_filepaths = []

    for filepath in filepaths:
        for filename in filename_search_list:
            if filename in filepath:
                matched_filepaths.append(filepath)

    return matched_filepaths
    

def search_terms(filepaths, search_terms_list):
    matched_filepaths = []

    for filepath in filepaths:
        with filepath.open() as opened_file:
            contents = opened_file.read()
            for term in search_terms_list:
                if term in contents:
                    matched_filepaths.append(filepath)

    return matched_filepaths
        

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory where search will be performed")
    parser.add_argument("-tl", "--terms", help="File with terms that will be searched for inside files")
    parser.add_argument("-fl", "--filenames", help="File with filenames to be searched for")

    args = parser.parse_args()
    variables = vars(args)

    search_terms = load_wordlist(variables['terms'])
    search_filenames = load_wordlist(variables['filenames'])

    found_filepaths = get_filepaths(variables['directory'])

    found_terms = search_terms(found_filepaths, search_terms)
    found_filenames = search_filenames(found_filepaths, search_filenames)

    print(found_terms)
    print(found_filenames)

if __name__ == '__main__':
    main()
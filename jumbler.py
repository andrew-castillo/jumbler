"""
Solve a jumble (anagram) by checking against each word in a dictionary
Authors: Andrew Castillo

Credits:
Python for Beginners
<http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python>
Section on opening a file.

Usage: python3 jumbler.py jumbleword wordlist.txt
"""

import argparse

def jumbler(jumble, dict_file_name):
    
    """
    Function takes the user-inputted jumble argument, and iterates through the specified
    text file, given by the innput dict_file_name. Sorts jumble and lines in the file,
    and checks if they are equal. Prints the matches, followed by the number of matches and
    number of words.
    
    args: jumble: a collection of letters, numbers, or characters inputted by the user
          dict_file_name: the file with which the contents of jumble will be compared    
    """

    f = open(dict_file_name, 'r') #opens the file
    
    sorted_jumble = sorted(jumble)
    counter_line = 0
    counter_match = 0
    
    for line in f:
        line = line.strip()
        sorted_line = sorted(line)
        counter_line += 1
        if sorted_line == sorted_jumble:
            print(line)
            counter_match += 1
            
    f.close() #closes the file
    
    if counter_match == 0:
        print('No matches')
    elif counter_match == 1:
        print('1 match in {} words'.format(counter_line))
    elif counter_match > 1:
        print('{} matches in {} words'.format(counter_match, counter_line))
            

def main():
    """
    collect command arguments and invoke jumbler()
    inputs:
        none, fetches arguments using argparse
    effects:
        calls jumbler()
    """
    parser = argparse.ArgumentParser(description="Solve a jumble (anagram)")
    parser.add_argument("jumble", type=str, help="Jumbled word (anagram)")
    parser.add_argument('wordlist', type=str,
                        help="A text file containing dictionary words, one word per line.")
    args = parser.parse_args()  # gets arguments from command line
    jumble = args.jumble
    wordlist = args.wordlist
    jumbler(jumble, wordlist)

if __name__ == "__main__":
    main()     

    

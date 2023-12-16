import argparse

def count_byte(file_path):
    try:
        # open the file in binary mode for easier processing
        with open(file_path, 'rb') as file:
            # read the content of file and get length in bytes
            byte_count = len(file.read())
            file.close()
            return byte_count
    except FileNotFoundError:
        print('error: File not found')
    

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            
            return sum(1 for line in file)
    except FileNotFoundError:
        print('error: File not found')

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            word_count = sum(len(line.split()) for line in file)
            return word_count
        
    except FileNotFoundError:
        print('error: File not found')

def count_characters(file_path):
    char_count = 0
    try:
        with open(file_path, 'r') as file:
                for line in file:
                    array_of_words = line.split()
                    for char in array_of_words:
                        char_count += len(char)

        return char_count
        
    except FileNotFoundError:
        print('error: File not found')

def main():

    # create argument parser
    arg_parser = argparse.ArgumentParser(description='ccwc Count args in file')
    # add commandline options
    arg_parser.add_argument('file_path', metavar='FILE', help='enter path to file')
    arg_parser.add_argument('-c', '--bytes', action='store_true', help='print the byte count')
    arg_parser.add_argument('-l', '--lines', action='store_true', help='print the lines count')
    arg_parser.add_argument('-w','--words', action='store_true', help='print the number of words in a file')
    arg_parser.add_argument('-m','--chars', action='store_true', help='print the number of characters in a file')

    # parse the commandline argument
    args = arg_parser.parse_args()
    #check if the '-c' option is provided
    if not (args.bytes or args.lines or args.words or args.chars):
        print('Please provide at least one of the options -c or -l or -w  or -m')
        return
    
    
    if args.chars:
        number_of_chars = count_characters(args.file_path)
        print(f'Number of characters in {args.file_path} is: {number_of_chars}')
    
    if args.words:
        number_of_words = count_words(args.file_path)
        print(f'Number of words in {args.file_path} is: {number_of_words}')
    
    if args.lines:
        number_of_lines = count_lines(args.file_path)
        print(f'Number of lines in {args.file_path} is: {number_of_lines}')

    if args.bytes:
        number_of_bytes = count_byte(args.file_path)
        print(f'Byte count in {args.file_path} is : {number_of_bytes}')
    

if __name__ == '__main__':
    main()
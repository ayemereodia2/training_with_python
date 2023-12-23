import json
import argparse

def parse_json_python(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            print('Parsed JSON object:', json_data)
    except FileNotFoundError:
        print(f'The file {file_path} does not exist')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from {file_path} the may not contain valid JSON')
    except Exception as e:
        print(f'An error occure {e}')

def parse_json_raw(file_path):
    try:
        with open(file_path, 'r') as file:
            json_text = file.read()
            # remove any white spaces
            json_text = ''.join(json_text.split())

            if json_text.startswith('{') and json_text.endswith('}'):
                json_text = json_text[1:-1] #[start: stop: step]
                # split into key-value pairs
                key_value_pairs = json_text.split(',')

                #extract and print key-value pairs
                for pair in key_value_pairs:
                    key,value = pair.split(':')
                    print(pair)
                    # key = key.strip('"').strip() # remove the quotes keys
                    # value = value.strip('"').strip() # remove the quotes from values
                    # print(f'Key: {key} and, Value {value}')

            else:
                print('File does not contain a valid JSON')
    except FileNotFoundError:
        print(f'The file {file_path} does not exist')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from {file_path} the may not contain valid JSON')
    except Exception as e:
        print(f'An error occured {e}')

# {
#     "" : "",
#     "": ""
# }

def main():

    # create argument parser
    arg_parser = argparse.ArgumentParser(description='ccwc Count args in file')
    # add commandline options
    arg_parser.add_argument('file_path', metavar='FILE', help='enter path to file')
    arg_parser.add_argument('-p', '--parse', action='store_true', help='parse json file')


    # parse the commandline argument
    args = arg_parser.parse_args()
    #check if the '-c' option is provided
    if not (args.parse):
        print('Please provide the options -p to parse')
        return
    
    
    if args.parse:
        object_found = parse_json_raw(args.file_path)
        print(f'Object found in JSON file {args.file_path} is: {object_found}')


if __name__ == '__main__':
    main()
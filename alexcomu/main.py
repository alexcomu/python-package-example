from configparser import ConfigParser
import argparse, os

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", type=str, help="Configuration file")
    args = parser.parse_args()
    return args

def program():

    print "Welcome to my package!"

    import globals
    globals.init()

    parsed_input = parse_input()
    parser = ConfigParser()
    parser.read(os.path.expanduser(parsed_input.config_file))

    print "Reading configuration: "
    import json
    slaves = json.loads(parser.get('ftp', 'alex'))
    print slaves.__class__
    print slaves

def main():
    try:
        program()
    except Exception as e:
        print e

if __name__ == "__main__":
    main()

import json
import os
import argparse
import pprint

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as raw_json_file:
        raw_json_file_text = json.load(raw_json_file)
        #return raw_json_file_text
        print(raw_json_file_text)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter filepath file')
    namespace = parser.parse_args()
    print(namespace)
    if namespace.path:
        load_data(namespace.path)

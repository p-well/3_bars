import json
import os
import argparse

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as raw_json_file:
        deserialized_json = json.load(raw_json_file)
        #return deserialized_json
        print(deserialized_json)

def get_biggest_bar(bars_data):
    max_seats_number = 0
    biggest_bar_name = str()
    for bar_info in load_data(bars_data):
        if bar_info.get('SeatsCount') > max_seats_number:
            max_seats_number = bar_info.get('SeatsCount')
    print(max_seats_number)

def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter filepath file')
    namespace = parser.parse_args()
    #print(namespace)
    if namespace.path:
        load_data(namespace.path)

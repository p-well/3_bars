import json
import os
import argparse

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as raw_json_file:
        deserialized_json = json.load(raw_json_file)
        return deserialized_json
        #print(deserialized_json)

def get_biggest_bar(bars_data):
    biggest_bar_data = max(bars_data, key = lambda bars: bars.get('SeatsCount'))
    #print(biggest_bar_data)
    print('Самый большой бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(biggest_bar_data.get('Name'),
               biggest_bar_data.get('SeatsCount'),
               biggest_bar_data.get('Address')
               )
        )
   

def get_smallest_bar(bars_data):
    smallest_bar_data = min(bars_data, key = lambda bars: bars.get('SeatsCount'))
    print('Самый маленький бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(smallest_bar_data.get('Name'),
               smallest_bar_data.get('SeatsCount'),
               smallest_bar_data.get('Address')
               )
        )

def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    moscow_bars = load_data('raw_json.json')
    get_biggest_bar(moscow_bars) 

    get_smallest_bar(moscow_bars)


    # parser = argparse.ArgumentParser()
    # parser.add_argument('-p','--path', required = True,
    #                     help = 'Enter filepath file')
    # namespace = parser.parse_args()
    # #print(namespace)
    # if namespace.path:
    #     #load_data(namespace.path)
    #     get_biggest_bar(load_data(namespace.path))

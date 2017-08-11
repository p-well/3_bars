import json
import os
import argparse
from math import sqrt

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as raw_json_file:
        deserialized_json = json.load(raw_json_file)
        return deserialized_json

def get_biggest_bar(bars_data):
    biggest_bar_data = max(bars_data, key = lambda bars: bars.get('SeatsCount'))
    return biggest_bar_data.get('Name'), biggest_bar_data.get('SeatsCount'), biggest_bar_data.get('Address')
    
def get_smallest_bar(bars_data):
    smallest_bar_data = min(bars_data, key = lambda bars: bars.get('SeatsCount'))
    return smallest_bar_data.get('Name'), smallest_bar_data.get('SeatsCount'), smallest_bar_data.get('Address')

def get_closest_bar(bars_data, latitude, longitude):
    x_user, y_user = latitude, longitude
    for bar_data in bars_data:
        x_bar, y_bar = float(bar_data.get('Latitude_WGS84')), float(bar_data.get('Longitude_WGS84'))
        distance = sqrt((x_bar - x_user)**2 + (y_bar - y_user)**2)
        bar_data['user_distance'] = distance
    closest_bar_data = min(bars_data, key = lambda bar: bar.get('user_distance'))
    print('\nБлижайший бар - это {}. Его адрес: {}.'.
        format(closest_bar_data.get('Name'), closest_bar_data.get('Address')))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file')
    namespace = parser.parse_args()
    moscow_bars_data = load_data(namespace.path)

    print('\nСамый большой бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(get_biggest_bar(moscow_bars_data)[0],
               get_biggest_bar(moscow_bars_data)[1],
               get_biggest_bar(moscow_bars_data)[2]))    

    print('\nА самый маленький бар называется "{}" и в нем {} мест. Его адрес: {}.'.
        format(get_smallest_bar(moscow_bars_data)[0],
               get_smallest_bar(moscow_bars_data)[1],
               get_smallest_bar(moscow_bars_data)[2]))


    print('''\nОк. Давай теперь найдем ближайший бар! Нужно ввести свои координаты -
широту и долготу. Например: 55.753215 и 37.622504.''')
    try:
        user_latitude = float(input("\nШирота:"))
        user_longitude = float(input("Долгота:"))
        get_closest_bar(moscow_bars_data, user_latitude, user_longitude)
    except ValueError as wrong_input_info:
        print(wrong_input_info)

import json
import os
import argparse
from geopy.distance import vincenty

def load_data(filepath):
    if not os.path.isfile(filepath):
        return None
    with open(filepath, 'r', encoding = 'cp1251') as raw_json_file:
        deserialized_json = json.load(raw_json_file)
        return deserialized_json

def get_biggest_bar(bars_data):
    biggest_bar_data = max(bars_data, key = lambda bars: bars.get('SeatsCount'))
    print('\nСамый большой бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(biggest_bar_data.get('Name'),
               biggest_bar_data.get('SeatsCount'),
               biggest_bar_data.get('Address')
               )
        )

def get_smallest_bar(bars_data):
    smallest_bar_data = min(bars_data, key = lambda bars: bars.get('SeatsCount'))
    print('А самый маленький бар называется "{}" и в нем {} мест. Его адрес: {}.'.
        format(smallest_bar_data.get('Name'),
               smallest_bar_data.get('SeatsCount'),
               smallest_bar_data.get('Address')
               )
        )

def get_closest_bar(bars_data, latitude, longitude):
    user_coordinates = (latitude, longitude)
    for bar_data in bars_data:
        bar_coordinates = (float(bar_data.get('Latitude_WGS84')), float(bar_data.get('Longitude_WGS84')))
        distance = vincenty(user_coordinates, bar_coordinates).km
        bar_data['user_distance'] = distance
    closest_bar_data = min(bars_data, key = lambda bar: bar.get('user_distance'))
    print('\nБлижайший бар - это {}. Его адрес: {}. До него {} километра'.
        format(closest_bar_data.get('Name'),
               closest_bar_data.get('Address'), 
               round(closest_bar_data.get('user_distance'),1))
        )    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path', required = True,
                        help = 'Enter path to file')
    namespace = parser.parse_args()
    if namespace.path:
        
        moscow_bars_data = load_data(namespace.path)
        get_biggest_bar(moscow_bars_data)
        get_smallest_bar(moscow_bars_data)

        print('''\nОк. Давай теперь найдем ближайший бар! Нужно ввести свои координаты -
широту и долготу. Например: 55.753215 и 37.622504.''')
        while True:
            try:
                user_latitude = float(input("\nШирота:"))
                user_longitude = float(input("Долгота:"))
                break
            except ValueError:
                print('\nТы ввел что-то не то, попробуй еще раз.')   
        get_closest_bar(moscow_bars_data, user_latitude, user_longitude)

    

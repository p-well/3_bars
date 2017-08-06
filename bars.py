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

    print('Самый большой бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(biggest_bar_data.get('Name'),
               biggest_bar_data.get('SeatsCount'),
               biggest_bar_data.get('Address')
               )
        )

def get_smallest_bar(bars_data):
    smallest_bar_data = min(bars_data, key = lambda bars: bars.get('SeatsCount'))

    print('А самый маленький бар в Москве - это "{}". В нем {} мест и находится он\nпо адресу: {}.'.
        format(smallest_bar_data.get('Name'),
               smallest_bar_data.get('SeatsCount'),
               smallest_bar_data.get('Address')
               )
        )

def get_closest_bar(bars_data, longitude, latitude):
    x_user = longitude
    y_user = latitude
    for bar_data in bars_data:
        x_bar = bar_data.get('Longitude_WGS84')
        y_bar = bar_data.get('Latitude_WGS84')
        distance = sqrt((x_user - x_bar)**2 + (y_user - y_bar)**2)
        bar_data['User_distance'] = distance
    closest_bar_data = min(bars_data, key = lambda bar: bar.get('User_distance'))
    print('Ближайший к вам бар - это {}. Его адрес {}'.
        format(closest_bar_data.get('Name'), closest_bar_data.get('Address')))    


if __name__ == '__main__':
    #load_data('raw_json.json')
    moscow_bars = load_data('raw_json.json')
    get_biggest_bar(moscow_bars) 
    get_smallest_bar(moscow_bars)
    user_longitude = float(input("Enter your longitude:"))
    user_latitude = float(input("Enter your latitude:"))
    get_closest_bar(moscow_bars, user_longitude, user_latitude)

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-p','--path', required = True,
    #                     help = 'Enter filepath file')
    # namespace = parser.parse_args()
    # #print(namespace)
    # if namespace.path:
    #     #load_data(namespace.path)
    #     get_biggest_bar(load_data(namespace.path))

# Nearest Moscow Bars

The program will help you to find the biggest and the smallest Moscow bars
as well as the closest bar to you.


# Quickstart

To run the program use the following commands in CLI:

```
python bars.py -p <filepath> 

or

python bars.py --page <filepath>

Filepath should be like:  C:\projects\devman\3_bars\moscow_bars.json
```
To find the nearest bar user have to input his GPS coordinates: latitude and longitude respectively.

3-rd party module 'geopy' is used. Run ```pip install -r requirements.txt``` to install the module.

The input data is retrieved from Moscow City Government Open Data [data.mos.ru](https://data.mos.ru/) in JSON format.

# Example of Script Launch

```
Самый большой бар в Москве - это "Спорт бар «Красная машина»". В нем 450 мест и находится он
по адресу: Автозаводская улица, дом 23, строение 1.
А самый маленький бар называется "БАР. СОКИ" и в нем 0 мест. Его адрес: Дубравная улица, дом 34/29.

Ок. Давай теперь найдем ближайший бар! Нужно ввести свои координаты -
широту и долготу. Например: 55.753215 и 37.622504.

Широта:55.679369
Долгота:37.704353

Ближайший бар - это БАР ПЕНА. Его адрес: проспект Андропова, дом 37. До него 2.6 километра.

```

# Project Goals

The code is written for educational purposes. Training course for web-developers -[DEVMAN.org](https://devman.org)

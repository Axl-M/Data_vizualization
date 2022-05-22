import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)      # объект чтения данных для файла
    # функция next(), возвращает следующую строку файла для полученного объекта чтения данных.
    # В следующем листинге функция next() вызывается только один раз для получения первой строки файла, содержащей заголовки
    header_row = next(reader)
    print(header_row)


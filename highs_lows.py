import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат, температурных максимумов и минимумов из файла.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)      # объект чтения данных для файла
    # функция next(), возвращает следующую строку файла для полученного объекта чтения данных.
    # В следующем листинге функция next() вызывается только один раз для получения первой строки файла, содержащей заголовки
    header_row = next(reader)
    # print(header_row)

# Заголовок AKDT означает «Alaska Daylight Time» (Аляска, летнее время).
# Позиция заголовка указывает на то, что первым значением в каждой из следующих строк является дата или время.

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:      # перебирает остальные строки в файле
        # Объект reader продолжает с того места, на котором он остановился в ходе чтения файла CSV,
        # и автоматически возвращает каждую строку после текущей позиции. Так как заголовок уже прочитан,
        # цикл продолжается со второй строки, в которой начинаются фактические данные.
        # При каждом проходе цикла значение с индексом 1 (второй столбец) присоединяется к списку highs
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))

# print(highs)
# нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Форматирование диаграммы.
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()     # вывод дат по диагонали
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
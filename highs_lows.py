import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
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

    # чтение максимальных температур из файла
    highs = []
    for row in reader:      # перебирает остальные строки в файле
        # Объект reader продолжает с того места, на котором он остановился в ходе чтения файла CSV,
        # и автоматически возвращает каждую строку после текущей позиции. Так как заголовок уже прочитан,
        # цикл продолжается со второй строки, в которой начинаются фактические данные.
        # При каждом проходе цикла значение с индексом 1 (второй столбец) присоединяется к списку highs
        highs.append(int(row[1]))

# print(highs)
# нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Форматирование диаграммы.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
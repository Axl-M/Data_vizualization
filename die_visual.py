from die import Die
import pygal

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Визуализация результатов.
hist =pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# Метод add() используется для добавления на гистограмму серии значений
# (при этом ему передается метка для добавляемого набора и список значений,
# отображаемых на диаграмме).
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')  # открывать в браузере

# интерактивность диаграмм, построенных с использованием Pygal:
# если навести указатель мыши на столбец диаграммы, вы увидите данные,
# связанные с этим столбцом. Данная возможность особенно полезна при
# нанесении нескольких наборов данных на одну диаграмму.
"""Создадим кубики с 6 и 10 гранями и посмотрим, что произойдет, если бросить их 50 000 раз """

from die import Die
import pygal

qty_sides_1 = input(' Сколько граней у первого кубика? ==> ')
qty_sides_2 = input(' Сколько граней у второго кубика? ==> ')
# Создание кубиков.
die_1 = Die(int(qty_sides_1))
die_2 = Die(int(qty_sides_2))

# Моделирование серии бросков с сохранением результатов в списке.
numbers_of_roll = input(' Сколько бросков смоделировать?  ==>')
results = [die_1.roll() + die_2.roll() for roll_num in range(int(numbers_of_roll))]

# Анализ результатов.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

# Визуализация результатов.
hist = pygal.Bar()
hist.title = f"Results of rolling a D{qty_sides_1} and a D{qty_sides_2}  {numbers_of_roll} times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add(f'D{qty_sides_1} + D{qty_sides_2}', frequencies)
hist.render_to_file('diff_dice_visual_2v.svg')

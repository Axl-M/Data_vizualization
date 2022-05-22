from die import Die

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_number in range(100):
    result = die.roll()
    results.append(result)

print(results)

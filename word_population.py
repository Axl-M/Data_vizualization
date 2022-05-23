import json

# Список заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Вывод населения каждой страны за 2010 год.
for pop_dict in pop_data:       # перебор словарей
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # float т.к. встречаются дробные значения (может интерполировали)
        print(country_name + ': ' + str(population))
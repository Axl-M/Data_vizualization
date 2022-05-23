import json
from country_codes import get_country_code

# Список заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Вывод населения каждой страны за 2010 год.
for pop_dict in pop_data:       # перебор словарей
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # float т.к. встречаются дробные значения (может интерполировали)
        # print(country_name + ': ' + str(population))

        # получаем для заданной страны ее код Pygal, состоящий из 2 букв. (т.к. в JSON 3-х буквенные коды)
        code = get_country_code(country_name)
        if code:
            print(code + ': ' + str(population))
        else:                                   # Если код недоступен
            print('ERROR - ' + country_name)
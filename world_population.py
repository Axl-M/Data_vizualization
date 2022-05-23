import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code

# Список заполняется данными.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Построение словаря с данными численности населения.
# Вывод населения каждой страны за 2010 год.
cc_populations = {}
for pop_dict in pop_data:       # перебор словарей
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # float т.к. встречаются дробные значения (может интерполировали)
        # print(country_name + ': ' + str(population))

        # получаем для заданной страны ее код Pygal, состоящий из 2 букв. (т.к. в JSON 3-х буквенные коды)
        code = get_country_code(country_name)
        if code:
            # print(code + ': ' + str(population))
            cc_populations[code] = population
        # else:                                   # Если код недоступен
        #     print('ERROR - ' + country_name)

# Группировка стран по 3 уровням населения.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:    # < 10 млн
        cc_pops_1[cc] = pop
    elif pop < 1000000000:  # < 1 млрд
        cc_pops_2[cc] = pop
    else:                   # > 1 млрд
        cc_pops_3[cc] = pop

# Проверка количества стран на каждом уровне.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# wm = pygal.maps.world.World()
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Мировая популяция в 2010, по странам'
wm.add('0-10 млн', cc_pops_1)
wm.add('10 млн-1 млрд', cc_pops_2)
wm.add('>1 млрд', cc_pops_3)



# wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')
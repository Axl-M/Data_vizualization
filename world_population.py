import json
import pygal
from pygal.style import RotateStyle as Rc
from pygal.style import LightColorizedStyle as Lcs
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

        # Получаем для заданной страны ее код Pygal, состоящий из 2 букв. (т.к. в JSON 3-х буквенные коды)
        code = get_country_code(country_name)
        if code:
            # print(code + ': ' + str(population))
            cc_populations[code] = population
        else:                                   # Если код недоступен
            print('ERROR - ' + country_name)

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

wm_style = Rc('#336699', base_style=Lcs)   # base_style для осветления темы
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'Мировая популяция в 2010, по странам'
wm.add('0-10 млн', cc_pops_1)
wm.add('10 млн-1 млрд', cc_pops_2)
wm.add('>1 млрд', cc_pops_3)

# wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')

#
# NOT FOUNDED
# ERROR - Arab World
# ERROR - Caribbean small states
# ERROR - East Asia & Pacific (all income levels)
# ERROR - East Asia & Pacific (developing only)
# ERROR - Euro area
# ERROR - Europe & Central Asia (all income levels)
# ERROR - Europe & Central Asia (developing only)
# ERROR - European Union
# ERROR - Heavily indebted poor countries (HIPC)
# ERROR - High income
# ERROR - High income: nonOECD
# ERROR - High income: OECD
# ERROR - Latin America & Caribbean (all income levels)
# ERROR - Latin America & Caribbean (developing only)
# ERROR - Least developed countries: UN classification
# ERROR - Low & middle income
# ERROR - Low income
# ERROR - Lower middle income
# ERROR - Middle East & North Africa (all income levels)
# ERROR - Middle East & North Africa (developing only)
# ERROR - Middle income
# ERROR - North America
# ERROR - OECD members
# ERROR - Other small states
# ERROR - Pacific island small states
# ERROR - Small states
# ERROR - South Asia
# ERROR - Sub-Saharan Africa (all income levels)
# ERROR - Sub-Saharan Africa (developing only)
# ERROR - Upper middle income
# ERROR - World
# ERROR - American Samoa
# ERROR - Antigua and Barbuda
# ERROR - Aruba
# ERROR - Bahamas, The
# ERROR - Barbados
# ERROR - Bermuda
# ERROR - Bolivia
# ERROR - Cayman Islands
# ERROR - Channel Islands
# ERROR - Comoros
# ERROR - Congo, Dem. Rep.
# ERROR - Congo, Rep.
# ERROR - Curacao
# ERROR - Dominica
# ERROR - Egypt, Arab Rep.
# ERROR - Faeroe Islands
# ERROR - Fiji
# ERROR - French Polynesia
# ERROR - Gambia, The
# ERROR - Gibraltar
# ERROR - Grenada
# ERROR - Hong Kong SAR, China
# ERROR - Iran, Islamic Rep.
# ERROR - Isle of Man
# ERROR - Kiribati
# ERROR - Korea, Dem. Rep.
# ERROR - Korea, Rep.
# ERROR - Kosovo
# ERROR - Kyrgyz Republic
# ERROR - Lao PDR
# ERROR - Libya
# ERROR - Macao SAR, China
# ERROR - Macedonia, FYR
# ERROR - Marshall Islands
# ERROR - Micronesia, Fed. Sts.
# ERROR - Moldova
# ERROR - New Caledonia
# ERROR - Northern Mariana Islands
# ERROR - Palau
# ERROR - Qatar
# ERROR - Samoa
# ERROR - Sint Maarten (Dutch part)
# ERROR - Slovak Republic
# ERROR - Solomon Islands
# ERROR - St. Kitts and Nevis
# ERROR - St. Lucia
# ERROR - St. Martin (French part)
# ERROR - St. Vincent and the Grenadines
# ERROR - Tanzania
# ERROR - Tonga
# ERROR - Trinidad and Tobago
# ERROR - Turks and Caicos Islands
# ERROR - Tuvalu
# ERROR - Vanuatu
# ERROR - Venezuela, RB
# ERROR - Vietnam
# ERROR - Virgin Islands (U.S.)
# ERROR - West Bank and Gaza
# ERROR - Yemen, Rep.
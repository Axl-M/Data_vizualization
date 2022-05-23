from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """ Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    # в JSON используются 3-х буквенные коды
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == 'Yemen, Rep.':
            return 'ye'

    # Если страна не найдена, вернуть None.
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))

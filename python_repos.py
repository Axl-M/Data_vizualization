"""
API запрос на GITHUB для вывода информации о проектах Python с наибольшим количеством звезд
https://api.github.com/search/repositories?q=language:python&sort=stars
 https://api.github.com/ -передает запрос части сайта GitHub, отвечающей на вызовы API.
Следующая часть, search/repositories, приказывает API провести поиск по всем репозиториям в GitHub.
? после repositories означает, что мы собираемся передать аргумент.
Символ q обозначает запрос (Query), а знак равенства начинает определение запроса (q=).
Выражение language:python указывает, что запрашивается информация только по репозиториям,
для которых основным языком указан Python.
Завершающая часть, &sort=stars, сортирует проекты по количеству присвоенных им звезд.
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)   # Код 200 — признак успешного ответа.

# Сохранение ответа API в переменной.
response_dict = r.json()

# Обработка результатов.
# print(response_dict.keys())     # ['total_count', 'incomplete_results', 'items']
# total_count - к-во найденных ответов на запрос
# incomplete_results - false если вызов завершился без ошибки
# items - список со словарями, каждый из которых содержит данные об одном репозитории Python
print("Total repositories:", response_dict['total_count'])  # общее количество репозиториев Python в GitHub

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']  # список словарей, каждый из которых содержит данные об одном репозитории Python
# print("Repositories returned:", len(repo_dicts))    # 30

# print("\nSelected information about each repository:")
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # print('\nName:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repository:', repo_dict['html_url'])
    # print('Description:', repo_dict['description'])

# построение визуализации
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

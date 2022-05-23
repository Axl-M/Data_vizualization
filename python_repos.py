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

# Создание вызова API и сохранение ответа.
url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)   # Код 200 — признак успешного ответа.

# Сохранение ответа API в переменной.
response_dict = r.json()

# Обработка результатов.
print(response_dict.keys())     # ['total_count', 'incomplete_results', 'items']
# total_count - к-во найденных ответов на запрос
# incomplete_results - false если вызов завершился без ошибки
# items - список со словарями, каждый из которых содержит данные об одном репозитории Python
print("Total repositories:", response_dict['total_count'])  # общее количество репозиториев Python в GitHub

# Анализ информации о репозиториях.
repo_dicts = response_dict['items'] # список со словарями, каждый из которых содержит данные об одном репозитории Python
print("Repositories returned:", len(repo_dicts))    # 30

# Анализ первого репозитория.
repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))    # 78
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

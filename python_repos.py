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
# items - список словарей со всеми данными


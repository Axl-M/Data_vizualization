"""
Получение идентификаторов статей, наиболее популярных на Hacker News (http://news.ycombinator.com/).
На этом сайте пользователи делятся друг с другом статьями, посвященными программированию и технологиям,
а также активно обсуждают эти статьи.
Этот вызов API возвращает список идентификаторов 500 самых популярных статей на Hacker News на момент выдачи вызова.
"""

import requests
from operator import itemgetter

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)        # Код 200 — признак успешного запроса.
# Обработка информации о каждой статье.
submission_ids = r.json()       # ответ преобразуется в список
submission_dicts = []           # список для хранения словарей.
for submission_id in submission_ids[:16]:  # для перебора идентификаторов 16 самых популярных статей
    # Создание отдельного вызова API для каждой статьи.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)     # проверить, успешно ли он был обработан.
    response_dict = submission_r.json()
    # словарь для текущей обрабатываемой статьи, в котором сохраняется заголовок статьи
    # и ссылка на страницу с ее обсуждением.
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)
# Отсортировать список словарей по количеству комментариев (itemgetter из operator).
# Сортируем список в обратном порядке, чтобы публикации с наибольшим количеством комментариев оказались на первом месте.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

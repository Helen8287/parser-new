#Задание 2: Параметры запроса
#Используйте API, который позволяет фильтрацию данных через URL-параметры
# (например, https://jsonplaceholder.typicode.com/posts).
#Отправьте GET-запрос с параметром userId, равным 1.
#Распечатайте полученные записи.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userId' : 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(post)
else:
    print("Error")

#Задание 1: Получение данных
#Импортируйте библиотеку requests.
#Отправьте GET-запрос к открытому API (например, https://api.github.com)
# с параметром для поиска репозиториев с кодом html.
#Распечатайте статус-код ответа.
#Распечатайте содержимое ответа в формате JSON.


import requests

url = "https://api.github.com/search/repositories"

params = {"q": "language:html"}

response = requests.get(url, params=params)

print(f"Status code: {response.status_code}")
print(response.json())

# Отправка данных.
#Используйте API, которое принимает POST-запросы для создания новых данных
# (например, https://jsonplaceholder.typicode.com/posts).
#Создайте словарь с данными для отправки
# (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
#Отправьте POST-запрос с этими данными.
#Распечатайте статус-код и содержимое ответа.



import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userId': 1,
    'title': 'foo',
    'body': 'bar'
}

response = requests.post(url, json=params)

print(response.status_code)

print(f"ответ - {response.json()}")

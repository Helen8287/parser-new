#Задание 3: Отправка данных
#Используйте API, которое принимает POST-запросы для создания новых данных
# (например, https://jsonplaceholder.typicode.com/posts).
#Создайте словарь с данными для отправки
# (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
#Отправьте POST-запрос с этими данными.
#Распечатайте статус-код и содержимое ответа.


import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

print (f"Status code: {response.status_code}")
print(f"ответ - {response.json()}")
import requests

# Задаем параметры запроса
params = {
    'userId': 1
}

# Отправляем GET-запрос с указанными параметрами
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

# Проверяем статус код ответа, чтобы убедиться, что запрос был успешным
if response.status_code == 200:
    # Преобразуем ответ в формат JSON и выводим его
    posts = response.json()

    # Печатаем каждую запись
    for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}, Body: {post['body']}\n")
else:
    print(f"Ошибка: не удалось получить данные, статус код {response.status_code}")
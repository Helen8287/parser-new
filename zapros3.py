import requests

# Отправляем GET-запрос для получения информации о пользователе с id 1
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Проверяем статус код ответа, чтобы убедиться, что запрос был успешным
if response.status_code == 200:
    # Преобразуем ответ в формат JSON и выводим его
    user = response.json()

    # Печатаем информацию о пользователе
    print(f"ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print(
        f"Address: {user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}")
    print(f"Phone: {user['phone']}")
    print(f"Website: {user['website']}")
    print(f"Company: {user['company']['name']}")
else:
    print(f"Ошибка: не удалось получить данные, статус код {response.status_code}")
import requests
import pprint

# Задаем параметры для поиска репозиториев, содержащих код на HTML
params = {
    'q': 'language:html'
}

# Отправляем GET-запрос к API GitHub с заданными параметрами
response = requests.get('https://api.github.com/search/repositories', params=params)

# Выводим статус-код ответа
print("Status Code:", response.status_code)

# Проверяем, что запрос был успешным
if response.status_code == 200:
    # Получаем содержимое ответа в формате JSON
    response_json = response.json()

    # Печатаем содержимое ответа
    pprint.pprint(response_json)
else:
    print("Failed to retrieve data")






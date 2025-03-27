import requests

params = {
    'userId' : 1
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)

print("Параметры запроса:", params)
print("JSON-ответ:", response.json())

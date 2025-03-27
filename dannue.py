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

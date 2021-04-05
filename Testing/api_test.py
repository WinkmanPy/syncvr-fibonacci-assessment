import requests

for i in range(101):
    api_url = f'http://127.0.0.1:5000/api/{i}' 
    result = requests.get(api_url)
    print(result.json())
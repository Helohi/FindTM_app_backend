import requests

BASE_URL = 'http://127.0.0.1:5000/'

if __name__ == '__main__':
    response1 = requests.get(BASE_URL)
    print(response1.json())

    response2 = requests.get(BASE_URL + 'google/google')
    print(response2.json())

    response3 = requests.get(BASE_URL+'google/google/1')
    print(response3.json())

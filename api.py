import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)


def dadJoke():
    joke_data = response.json()
    joke = joke_data["joke"]
    return joke

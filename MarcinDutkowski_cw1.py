import requests
import json

def get_data(url):
	try:
		answer = requests.get(url)
		answer.raise_for_status()
		data = answer.json()
		return data
	except requests.exceptions.HTTPError as wrong_url:
		print("Niewłaściwy adres!", wrong_url)
		return None


url = "https://httpbin.org/post"
headers = {'Content-Type': 'application/json'}
data = {
	"name": "natalia"
}

if data:
	print(data)
else:
	print("Niewłaściwy adres strony :(")

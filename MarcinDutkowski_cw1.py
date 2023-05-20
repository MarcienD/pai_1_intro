import requests

def get_data(url):
	try:
		answer = requests.get(url)
		answer.raise_for_status()
		data = answer.json()
		return data
	except requests.exceptions.HTTPError as wrong_url:
		print("Niewłaściwy adres!", wrong_url)
		return None


superheroes_url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
data = get_data(superheroes_url)
if data:
	print(data)
else:
	print("Niewłaściwy adres strony :(")

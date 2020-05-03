import requests

fact_endpoint = 'https://uselessfacts.jsph.pl/random.json'

def return_fact():
	while True:
		r = requests.get(fact_endpoint)
		r.json()
		if r.json()['language'] == 'en' and len(r.json()['text']) < 200:
			fact = r.json()['text']
			break
		else:
			print(f'Denied fact: {r.json()["text"]}')
	return fact

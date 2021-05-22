import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
# print(json)
# print(json.get("people"))

for person in json.get("people"):
    print(person['name'])

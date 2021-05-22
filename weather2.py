import requests

city='Buenos Aires'
api_key = '1368d72fe8a70a5a39722a181d9ce812'

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + api_key + "&units=metric"

request = requests.get(url)
json = request.json()
# print(json)

description = json.get("weather")[0].get("description")
print("Today's forecast is", description)

temp_min = json.get("main").get("temp_min")
print("The minimun temprature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("The maximum temprature is", temp_max)
 

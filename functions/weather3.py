import requests

def get_weahter_desc_and_temp():
    city='Buenos Aires'
    api_key = '##'

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + api_key + "&units=metric"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }

def main():
    weather_dict = get_weahter_desc_and_temp()
    # print the results
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimun temprature is", weather_dict.get('temp_min'))
    print("The maximum temprature is", weather_dict.get('temp_max'))


main()

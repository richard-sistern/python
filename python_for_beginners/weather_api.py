import requests

api_key = "bla...bla"
city = "Orlando"
url = "http://api.openweathermap.oreg/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forecase is", description)

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)
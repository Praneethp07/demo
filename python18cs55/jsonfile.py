#reading json values using loads() function
import json
from bs4 import BeautifulSoup
from requests import request

cityname = ""

cityname = str(input("Enter the place name:\n"))
url = f"https://open-weather13.p.rapidapi.com/city/{cityname}"

headers = {
	"X-RapidAPI-Key": "3183922243msha93bf5f6682c01fp1d5c51jsnd707180fcc5c",
	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = request("GET", url, headers=headers)

data  = json.loads(response.content)
temprature = data['main']['temp']
humidity = data['main']['humidity']
latitude = data['coord']['lat']
longitude =data['coord']['lon']
print(f"temprature:{temprature}^C\nhumidity:{humidity}\nlatittude:{latitude}\nlongitude:{longitude}")




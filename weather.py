from pydoc import tempfilepager
from wsgiref.util import request_uri
import requests

API_KEY = "57dfe52935932616c4b960616312e071"

BASE_URL = "https://openweathermap.org/"

city = input("Enter city:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature)

else:
    print("Error!!")


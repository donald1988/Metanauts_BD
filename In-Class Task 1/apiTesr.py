import json
import requests

url = "https://rapidapi.com/natkapral/api/countries-cities/ + countries"

headers = {
    'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    'x-rapidapi-key': "5bde482e7fmshfb67387ed5218a7p1d29dfjsn586c97707a7f"
    }

response = requests.request("GET", url, headers=headers)
print(response.text)

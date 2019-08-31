from pprint import pprint
import json
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5128638&APPID=931815b434162ebf2b86ca6f63abea55&units=imperial')

rj = r.json()
pprint(r.json())

pprint(int(round(rj["main"]["temp"])))

import requests

def get_temp():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4138106&APPID=931815b434162ebf2b86ca6f63abea55&units=imperial')

    rj = r.json()

    current_temp = int(round(rj["main"]["temp"]))

    print(current_temp)
            
    return current_temp;
    



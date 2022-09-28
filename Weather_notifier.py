
from bs4 import BeautifulSoup

import requests

import time

from win10toast import ToastNotifier


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):

    city=city.replace(" ","+")

    res = requests.get(f'https://www.google.com/search?q=visakhapatnam-weather&oq=visakhapatnam-weather&aqs=chrome..69i57.5791j0j1&sourceid=chrome&ie=UTF-8',headers=headers)
   
    soup = BeautifulSoup(res.text,'html.parser')

    location = soup.select('#wob_loc')[0].getText().strip()  

    current_time = soup.select('#wob_dts')[0].getText().strip() 

    info = soup.select('#wob_dc')[0].getText().strip() 

    weather = soup.select('#wob_tm')[0].getText().strip()

    information = f"{location} \n {current_time} \n {info} \n {weather} °C 🌤️"

        
    toaster = ToastNotifier()

    toaster.show_toast("Weather Reports 🌡️🌤️⛈️ for you 👇 Darling 👻👸  ",

    f"{information}",

    duration=30,

    threaded=True)

    while toaster.notification_active(): time.sleep(1700)   
    

#print("enter the city name")

#city=input()

city = "Visakhapatnam"

city=city+" weather"

weather(city)


'''import requests

from bs4 import BeautifulSoup

from win10toast import ToastNotifier

n = ToastNotifier() 

def getdata(url):
    
    r = requests.get(url)
      
    return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/065c1d3375d4c3a4117e2997bbf2d9eb44a8a7b5613c83796060362b1d8bbe20")
  
soup = BeautifulSoup(htmldata, 'html.parser')
  
print(soup.prettify())

current_temp = soup.find_all("span", 
                             class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div", 
                             class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
  
temp = (str(current_temp))   
temp_rain = str(chances_rain)
  
result = "Temperature in your area is" + temp[128:-9] + "℃  in Vizag 🏖️" + "\n" +temp_rain[131:-14]
n.show_toast("Live Weather update",  result, duration = 20)'''
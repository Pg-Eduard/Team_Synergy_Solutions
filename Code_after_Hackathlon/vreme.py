
import requests
import sys
import pandas as pd
import csv


response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Sibiu?unitGroup=metric&include=days&key=EM8HY5QB29WDGNP28PKVQR5NV&contentType=csv")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  

def get_vreme():
    temp,temp1 = "",""
    CSVText = csv.reader(response.text.splitlines(), delimiter=',',quotechar='"')

    df = pd.DataFrame(CSVText)

    #df.to_excel("static/vreme.xlsx",index=False)

    feelslike, humidity, sunrise, sunset, icon,temp_max,temp_min = df[7][1],df[9][1],df[26][1],df[27][1],df[31][1],df[2][1],df[3][1]

    for i in range(len(sunrise)):
       if i >= 11:
          temp += sunrise[i]
          temp1 += sunset[i]

    sunrise = temp
    sunset = temp1

    obj = {
        "feelslike": feelslike,
        "humidity": humidity,
        "sunrise": sunrise,
        "sunset": sunset,
        "icon": icon,
        "temp_max": temp_max,
        "temp_min": temp_min
    }

    return obj
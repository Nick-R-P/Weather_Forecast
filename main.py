import requests

url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Toronto/1970-01-01/2023-12-31?unitGroup=metric&include=days&key=S5M4GPEF3GL24ACA5VQ9CC2ES&contentType=json"
# params = {
#     "lat": 43.7001,
#     "lon": -79.4163,
#     "appid": "4ad38e4a7beaf6c26ee653ce4f655a0c"
# }

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP errors

    data = response.json()
    print(data)  # Print the entire response data for inspection

except requests.exceptions.RequestException as e:
    print("Error:", e)

import json

# Your JSON data as a string
# json_data = '''
# [
#     {
#         "date": "2023-03-23",
#         "date_epoch": 1679529600,
#         "day": {
#             "maxtemp_c": 7.0,
#             "maxtemp_f": 44.6,
#             "mintemp_c": 2.3,
#             "mintemp_f": 36.1,
#             "avgtemp_c": 4.8,
#             "avgtemp_f": 40.7,
#             "maxwind_mph": 11.0,
#             "maxwind_kph": 17.6,
#             "totalprecip_mm": 16.7,
#             "totalprecip_in": 0.66,
#             "totalsnow_cm": 0.0,
#             "avgvis_km": 6.0,
#             "avgvis_miles": 3.0,
#             "avghumidity": 92,
#             "daily_will_it_rain": 1,
#             "daily_chance_of_rain": 100,
#             "daily_will_it_snow": 0,
#             "daily_chance_of_snow": 0,
#             "condition": {
#                 "text": "Moderate or heavy rain with thunder",
#                 "icon": "//cdn.weatherapi.com/weather/64x64/day/389.png",
#                 "code": 1276
#             },
#             "uv": 2.0
#         }
#     }
# ]
# '''

# Convert JSON string to Python list
data_list = json.loads(data)

print(data)
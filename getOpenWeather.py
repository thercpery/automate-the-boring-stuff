#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = "314885947251cb11035a250d0a8b9c3f"

import json, requests, sys, pprint

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
location = " ".join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = "http://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s" % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text.
# print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
print(pprint.pformat(weatherData))

# Print weather descriptions.
w = weatherData["list"]
print(f"Current weather in {location}:")
print(w[0]["weather"][0]["main"], " - ", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], " - ", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], " - ", w[2]["weather"][0]["description"])
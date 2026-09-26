
import urllib.request as ub
import json
import sys
# First makes it so we find how many hours away are we from this
# So we can look that up in the dictionary
def first():
    origin = data["hourly"]["time"][0]
    originp = origin.split('-')
    origin2 = originp[2].split("T")[0]
    monthaccount = 30 - int(origin2)
    if origin > dates[0] and int(dates[1]) <= int(originp[1]):
        print("sorry you cannot look up dates in the past")
        sys.exit()
    if origin2 > dates[0]:
        dates[0] = int(dates[0]) + int(origin2) + monthaccount
    time1 = int(dates[0]) - int(origin2)
    time1 = time1 * 24
    time1 = time1 + hour
    if time1 > 143:
        print("sorry the program only goes up 5 days away at 23:00")
        sys.exit()
    datetime = data["hourly"]["time"][time1]
    temps = data["hourly"]["temperature_2m"][time1]
    print(f"the time is {datetime} and the temperature in {url} is {temps} degrees C")


url_westhill = "https://api.open-meteo.com/v1/forecast?latitude=57.1526&longitude=-2.2797&hourly=temperature_2m"
url_edinburgh = "https://api.open-meteo.com/v1/forecast?latitude=55.9521&longitude=-3.1965&hourly=temperature_2m"
url_london = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m"
url_nyc = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&hourly=temperature_2m"
url = input("Where do you want the weather (please pick Westhill, Edinburgh, London or NYC)")
if url == "Westhill":
     with ub.urlopen(url_westhill) as response:
         raw_data = response.read().decode("utf-8")
         data = json.loads(raw_data)
elif url == "Edinburgh":
    with ub.urlopen(url_edinburgh) as response:
         raw_data = response.read().decode("utf-8")
         data = json.loads(raw_data)
elif url == "London":
     with ub.urlopen(url_london) as response:
        raw_data = response.read().decode("utf-8")
        data = json.loads(raw_data)
elif url == "NYC":
    with ub.urlopen(url_nyc) as response:
         raw_data = response.read().decode("utf-8")
         data = json.loads(raw_data)

date = input("What is the date you want the temperature for (in dd/mm/yyyy format)")
hour = int(input("What hour do you want the temperature for (between 0 - 23)"))
dates = date.split('/')
first()



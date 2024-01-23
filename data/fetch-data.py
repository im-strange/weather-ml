
from datetime import datetime
from meteostat import Point, Daily, Hourly

start = datetime(2001, 1, 1)
end = datetime(2023, 12, 31)

location = Point(14.5585549, 121.1360819, 70)
data = Daily(location, start, end)
data = data.fetch()
data.to_csv("raw-weather.csv")

print("saved!")

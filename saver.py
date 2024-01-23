
import pickle
import csv

def save_pickle(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
        print(f"[+] {filename} successfully created")

data = list(csv.reader(open("data/weather.csv")))
columns = data[0]
data = data[1:]

#time = [int(i[0]) for i in data]
#temp = [float(i[1]) for i in data]
#humidity = [float(i[2]) for i in data]
#wind_direction = [float(i[3]) for i in data]
#wind_speed = [float(i[4]) for i in data]
label = [0 if float(i[5]) <= 6 else 1 for i in data]

#save_pickle("time.pickle", time)
#save_pickle("temp.pickle", temp)
#save_pickle("humidity.pickle", humidity)
#save_pickle("wind-dir.pickle", wind_direction)
#save_pickle("wind-spd.pickle", wind_speed)
save_pickle("label.pickle", label)

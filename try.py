
import math
import csv
import pickle
import random
import numpy as np
import pandas as pd
from function import load
from model import WeatherNB
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
from sklearn.metrics import r2_score
from scipy.stats import pearsonr

def reshape(array):
    array = np.array(array)
    array = array.reshape(-1, 1)
    return array

time = load("data/time.pickle")
temp = load("data/temp.pickle")
wind_spd = load("data/wind-spd.pickle")
wind_dir = load("data/wind-dir.pickle")
humidity = load("data/humidity.pickle")
label = load("data/label.pickle")

data = pd.read_csv("data/weather.csv")

X = data[
y = humidity
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
#report = classification_report(y_test, predictions)
score, p = pearsonr(humidity, label)
#print(report)
print(score)
#model.save("time-label.pickle")


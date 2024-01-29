
import math
import csv
import sys
import os
import pickle

import random
import numpy as np
import pandas as pd
from function import load
from function import check_pearsonr
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

time = load("time.pickle")
temp = load("temp.pickle")
wind_spd = load("wind-spd.pickle")
wind_dir = load("wind-dir.pickle")
humidity = load("humidity.pickle")
label = load("label.pickle")

data = [time, temp, wind_spd, wind_dir, humidity, label]
#data = pd.read_csv("data/weather.csv")

check_pearsonr(data)

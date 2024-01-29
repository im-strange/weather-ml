
import sys
import pickle
from scipy.stats import pearsonr

path = "data/hourly/"

def load(filename):
    with open(path+filename, "rb") as file:
        loaded = pickle.load(file)
        return loaded

def save_pickle(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print(f"{filename} successfully created!")

def check_pearsonr(datalist):
    for x in datalist:
        for y in datalist:
            if x != y:
                score, p = pearsonr(x, y)
                print(f"{datalist.index(x)} x {datalist.index(y)} : {score}")

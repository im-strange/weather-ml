
import sys
import pickle

def load(filename):
    with open(filename, "rb") as file:
        loaded = pickle.load(file)
        return loaded

def save_pickle(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
    print(f"{filename} successfully created!")


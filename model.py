
import pickle
import random
import csv
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class WeatherNB:
    def __init__(self):
        self.features = None
        self.labels = None
        self.test_features = None
        self.test_labels = None
        self.alpha = 1
        self.model = GaussianNB(var_smoothing=self.alpha)

    def fit(self, features, labels):
        self.features = features
        self.labels = labels

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.features,
            self.labels,
        )

        self.model.fit(self.X_train, self.Y_train)
        self.predictions = self.model.predict(self.X_test)
        self.report = classification_report(self.Y_test, self.predictions, zero_division=0)

    def predict(self, features):
        pass

    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.model, file)
            print(f"[+] model successfully saved to {filename}")

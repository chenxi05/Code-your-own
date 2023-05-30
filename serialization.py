#serialzation file
import pickle

from os import path

def save(object, file):
    if path.exists(file):
        with open(file, "wb") as f:
            pickle.dump(object, f)

def load(file):
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None


USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
    users = {}
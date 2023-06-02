#serialzation file
import pickle
import game
from os import path

def save(user_name, pts):
    if path.exists(user_name):
        with open(user_name, "wb") as f:
            pickle.dump(user_name, f)

def load(file):
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None

USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
    users = {}

def print():
    print("hello")
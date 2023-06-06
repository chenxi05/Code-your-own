#serialzation file
import pickle
from os import path

def save(user_info, USER_FILE):
    with open(USER_FILE, "wb") as f:
        pickle.dump(user_info, f)

def load(file):
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None

USERS_FILE = "user_info.pkl"
user_info = load(USERS_FILE)
if user_info is None:
    user_info = {}

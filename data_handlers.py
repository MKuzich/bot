import pickle

FILE_NAME = 'data.bin'

def save_data(data):
    global FILE_NAME
    with open(FILE_NAME, "wb") as fh:
        pickle.dump(data, fh)

def load_data():
    global FILE_NAME
    with open(FILE_NAME, "rb") as fh:
        return pickle.load(fh)
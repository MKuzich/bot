import pickle

file_name = 'data.bin'

def save_data(data):
    global file_name
    with open(file_name, "wb") as fh:
        pickle.dump(data, fh)

def load_data():
    global file_name
    with open(file_name, "rb") as fh:
        return pickle.load(fh)
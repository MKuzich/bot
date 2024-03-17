import pickle

FILE_NAME = "data.bin"


def save_data(contacts, notes_manager, counter):
    data_to_save = {
        "contacts": contacts,
        "notes_manager": notes_manager,
        "counter": counter,
    }
    global FILE_NAME
    with open(FILE_NAME, "wb") as fh:
        pickle.dump(data_to_save, fh)


def load_data():
    global FILE_NAME
    with open(FILE_NAME, "rb") as fh:
        data = pickle.load(fh)
    contacts = data["contacts"]
    notes_manager = data["notes_manager"]
    counter = data["counter"]
    return contacts, notes_manager, counter

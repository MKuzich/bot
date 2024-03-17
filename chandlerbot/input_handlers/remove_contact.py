from chandlerbot.input_error import input_error
from chandlerbot.errors import NameIsString

@input_error
def remove_contact(name, contacts):
    if not name.isalpha():
        raise NameIsString
    contacts.delete(name)
    return f"{name} removed."

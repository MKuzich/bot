from chandlerbot.input_error import input_error
from chandlerbot.errors import NameIsString


@input_error
def remove_birthday(name, contacts):
    """Removing address form contact record"""
    if name not in contacts:
        raise KeyError
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.remove_birthday()
    return "Birthday has been deleted."

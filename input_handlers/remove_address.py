from input_error import input_error
from errors import NameIsString


@input_error
def remove_address(name, contacts):
    """Removing address form contact record"""
    if name not in contacts:
        raise KeyError
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.remove_address()
    return "Address has been deleted."

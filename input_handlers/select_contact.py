from input_error import input_error
from errors import NameIsString


@input_error
def select_contact(args, contacts):
    _, name = args
    if not name.isalpha():
        raise NameIsString
    record = contacts.find(name)
    return record

from input_error import input_error
from errors import NameIsString

@input_error
def show_contact(args, contacts):
    name = args[0]
    if not name.isalpha():
        raise NameIsString
    return contacts.find(name)
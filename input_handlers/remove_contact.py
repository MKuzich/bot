from input_error import input_error
from errors import NameIsString

@input_error
def remove_contact(args, contacts):
    name = args[0]
    if not name.isalpha():
        raise NameIsString
    contacts.delete(name)
    return f"{name} removed."
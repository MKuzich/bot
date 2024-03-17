from input_error import input_error
from errors import NameIsString


@input_error
def remove_email(name, contacts):
    """Removing email form contact record"""
    if name not in contacts:
        raise KeyError
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.remove_email()
    return "Email has been deleted."

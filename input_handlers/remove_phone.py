from input_error import input_error
from errors import NameIsString


@input_error
def remove_phone(args, contacts):
    """Removing phone form contact record"""
    name, phone = args
    if name not in contacts:
        raise KeyError
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.remove_phone(phone)
    contacts.add_record(record)
    return "Phone has been deleted."

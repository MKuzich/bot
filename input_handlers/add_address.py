"""File for add address"""
from input_error import input_error
from errors import NameIsString

@input_error
def add_address(args, contacts):
    """Add address to record"""
    name, street, building, city, *additional = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.add_address(street, building, city, *additional)
    return f"{name}'s address added."

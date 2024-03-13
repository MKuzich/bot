"""File for add address"""
from input_error import input_error
from errors import NameIsString

@input_error
def show_address(args, contacts):
    """Add address to record"""
    name, *_ = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    return f"{record.address}"

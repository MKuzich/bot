"""File for add email functions"""
from input_error import input_error
from errors import NameIsString

@input_error
def add_email(args, contacts):
    """Add email to record"""
    name, email = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.add_email(email)
    return f"{name}'s email added."

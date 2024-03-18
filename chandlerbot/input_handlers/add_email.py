"""File for add email functions"""
from chandlerbot.input_error import input_error
from chandlerbot.errors import NameIsString

@input_error
def add_email(args, contacts):
    """Add email to record"""
    name, email = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    record.add_email(email)
    return f"{name}'s email added."

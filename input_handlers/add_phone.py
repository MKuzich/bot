from input_error import input_error
from errors import NotValidPhoneNumber, NameIsString


@input_error
def add_phone(args, contacts):
    """Adding new other phone to contact record"""
    name, phone = args
    if name not in contacts:
        raise KeyError
    if not phone.isdigit() or len(phone) != 10:
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString
    record = contacts.find(name)
    try:
        if record.find_phone(phone):
            return "Phone alredy in list."
    except IndexError:
        pass
    record.add_phone(phone)
    contacts.add_record(record)
    return "Phone has been added."

from input_error import input_error
from models import Record
from errors import NotValidPhoneNumber, NameIsString

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not phone.isdigit() or len(phone) != 10:
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"{name} with phone {phone} added."

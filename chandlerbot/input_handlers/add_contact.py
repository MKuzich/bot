from chandlerbot.input_error import input_error
from chandlerbot.models import Record
from chandlerbot.errors import NotValidPhoneNumber, NameIsString
from chandlerbot.models.phone import Phone

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not Phone(phone):
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"{name} with phone {phone} added."

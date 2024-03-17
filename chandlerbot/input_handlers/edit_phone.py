from chandlerbot.input_error import input_error
from chandlerbot.errors import NotValidPhoneNumber, NameIsString


@input_error
def edit_phone(contacts, name, phone, new_phone=None):
    if name not in contacts:
        raise KeyError
    if not phone.isdigit() or len(phone) != 10:
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    if len(record.phones) == 1:
        new_phone = phone
        phone = record.phones[0].value
    record.edit_phone(phone, new_phone)
    return f"{name} phone changed to {phone}."

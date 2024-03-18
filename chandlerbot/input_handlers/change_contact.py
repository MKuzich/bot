from chandlerbot.input_error import input_error
from chandlerbot.errors import NotValidPhoneNumber, NameIsString

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    if not phone.isdigit() or len(phone) != 10:
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString
    
    record = contacts.find(name)
    record.edit_phone(record.phones[0].value, phone)
    return f"{name} phone changed to {phone}."
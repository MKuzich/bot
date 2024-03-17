from chandlerbot.input_error import input_error
from chandlerbot.errors import NameIsString, NotValidDate

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    if birthday.count('.') != 2 or len(birthday) != 10 or not birthday.replace('.', '').isdigit():
        raise NotValidDate

    record.add_birthday(birthday)
    return f"{name}'s birthday added."
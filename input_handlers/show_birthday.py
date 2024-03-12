from input_error import input_error
from errors import NoBirthday, NameIsString

@input_error
def show_birthday(args, contacts):
    name = args[0]
    if not name.isalpha():
        raise NameIsString
    record = contacts.find(name)
    if not hasattr(record, 'birthday'):
        raise NoBirthday
    return record.birthday.value.strftime("%d %B, %Y")

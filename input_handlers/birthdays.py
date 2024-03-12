from input_error import input_error
from errors import NoBirthdays

@input_error
def birthdays(contacts):
    birthdays = contacts.get_birthdays_per_week()
    if not birthdays:
        raise NoBirthdays
    res = []
    for key, val in birthdays.items():
        res.append(f'{key}: {", ".join(val)}')
    return '\n'.join(res)
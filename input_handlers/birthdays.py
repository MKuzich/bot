"""Output contacts table"""
from tabulate import tabulate
from input_error import input_error
from errors import NoBirthdays,LimitSearchBirthdays

@input_error
def birthdays(args, contacts):
    days = int(args[0])
    if days > 365:
        raise LimitSearchBirthdays

    birthdays_contact = contacts.get_upcoming_birthdays(days)

    data_for_table = []
    for date, info in birthdays_contact.items():
        for day, name, phones, email, address in info:
            phones = phones or '?'
            email = email or '?'
            address = address or '?'

            data_for_table.append([date, day, name, phones, email, address])

    if not data_for_table:
        raise NoBirthdays

     #missingval do not working with maxcolwidths if one of element is None
    return "\n" + tabulate(data_for_table,
                    headers=['Date', 'Day', 'Name', 'Phones', 'Email', 'Address'], tablefmt="grid", missingval="?", maxcolwidths=[None, 30, 30, 30, 30]) + "\n"

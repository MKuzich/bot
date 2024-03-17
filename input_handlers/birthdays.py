"""Output contacts table"""
from helpers.table_output import table_output
from input_error import input_error
from errors import NoBirthdays,LimitSearchBirthdays

@input_error
def birthdays(args, contacts):
    """Output contacts birthdays"""
    days = int(args[0]) if args else int(7)
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

    #settings for tabulate
    headers = ['Date', 'Day', 'Name', 'Phones', 'Email', 'Address']
    tablefmt="grid"
    missingval="?"
    maxcolwidths=[None, 30, 30, 30, 30]

    caption = "By default, birthdays are shown 7 days in advance.\nIf you want a different number, then enter, example >>> birthdays 20\n\n" if not args else ""

    return table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths, caption)

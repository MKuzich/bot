"""Output contacts table"""
from tabulate import tabulate
from input_error import input_error
from errors import NoBirthdays

@input_error
def birthdays(args, contacts):
    days = int(args[0])
    if days > 365:
        return f"\nEnter a date less than 365 days\n"

    birthdays_contact = contacts.get_upcoming_birthdays(days)

    # Підготовка даних для виведення
    data_for_table = []
    for date, info in birthdays_contact.items():
        for day, name, phones, email, address in info:
            data_for_table.append([date, day, name, phones, email, address])

    if not data_for_table:
        return f"\nThere are no birthdays in the specified period\n"

    return "\n" + tabulate(data_for_table,
                    headers=['Date', 'Day', 'Name', 'Phones', 'Email', 'Address'], tablefmt="grid", missingval="?") + "\n"

"""Output contacts table"""
from tabulate import tabulate
from input_error import input_error
from errors import NoBirthdays

@input_error
def birthdays(args, contacts):
    days = args[0]
    birthdays_contact = contacts.get_upcoming_birthdays(days)

    # Підготовка даних для виведення
    data_for_table = []
    for date, info in birthdays_contact.items():
        for day, name, phones, email in info:
            data_for_table.append([date, day, name, phones, email])

    # Використання tabulate для виведення даних у вигляді таблички
    return tabulate(data_for_table,
                    headers=['Date', 'Day', 'Name', 'Phones', 'Email', 'Address'], tablefmt="grid")

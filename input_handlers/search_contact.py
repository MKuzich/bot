from tabulate import tabulate
from input_error import input_error
from errors import EmptyArgsContact, NoContacts

@input_error
def search_contact(args, contacts):
    if not args:
        raise EmptyArgsContact

    name = args[0]

    data_for_table = []
    for user in contacts.search_by_any(name):
        name = user.name.value
        email = user.email.value if user.email else None
        phones = ", ".join([phone.value for phone in user.phones]) if user.phones else None
        birthday = user.birthday.value.strftime('%d %B, %Y') if hasattr(user, 'birthday') and user.birthday else None
        address = str(user.address) if hasattr(user, 'address') and user.address else None
        data_for_table.append([name, phones, email, birthday, address])

    if not data_for_table:
        raise NoContacts

    return "\n" + tabulate(data_for_table, headers=['Name', 'Phones', 'Email', 'Birthday', 'Address'], tablefmt="grid", missingval="?", maxcolwidths=[None, 30, 30, 30, 30]) + "\n"

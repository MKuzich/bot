from tabulate import tabulate
from input_error import input_error
from errors import NoContacts

@input_error
def all_contacts(contacts):
    if not contacts:
        raise NoContacts

    data_for_table = []

    for contact in contacts.data.values():
        name = contact.name
        phones = ', '.join(str(phone) for phone in contact.phones) if contact.phones else '?'
        email = contact.email if contact.email else '?'
        address = contact.address if contact.address else '?'
        birthday = contact.birthday if contact.birthday else '?'

        data_for_table.append([name, phones, email, address, birthday])

    if not data_for_table:
        raise NoContacts

    #missingval do not working with maxcolwidths if one of element is None
    table = "\n" + tabulate(data_for_table, headers=['Name', 'Phones', 'Email', 'Address', 'Birthday'], tablefmt="grid", missingval="?", maxcolwidths=[None, 30, 30, 30, 30]) + "\n"

    return table

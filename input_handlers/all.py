from input_error import input_error
from errors import NoContacts

@input_error
def all(contacts):
    if not contacts:
        raise NoContacts
    all_contacts = []
    for i in contacts.data.values():
        all_contacts.append(str(i))
    
    return '\n'.join(all_contacts)
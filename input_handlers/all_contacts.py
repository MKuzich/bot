from input_error import input_error
from errors import NoContacts

@input_error
def all_contacts(contacts):
    if not contacts:
        raise NoContacts
    all_contacts_list = []
    for i in contacts.data.values():
        all_contacts_list.append(str(i))
    
    return '\n'.join(all_contacts)
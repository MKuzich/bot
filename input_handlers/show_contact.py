from helpers.table_output import table_output
from input_error import input_error
from errors import NameIsString

@input_error
def show_contact(args, contacts):
    name = args[0]
    if not name.isalpha():
        raise NameIsString
    
    data_for_table = []

    for user in contacts.find_by_name(name):
        name = user.name.value
        email = user.email.value if user.email else "?"
        phones = ", ".join([phone.value for phone in user.phones]) if user.phones else "?"
        birthday = user.birthday.value.strftime('%d %B, %Y') if hasattr(user, 'birthday') and user.birthday else "?"
        address = str(user.address) if hasattr(user, 'address') and user.address else "?"
        
        data_for_table.append([name, phones, email, address, birthday])

    #settings for tabulate
    headers=['Name', 'Phones', 'Email', 'Address', 'Birthday']
    tablefmt="grid"
    missingval="?"
    maxcolwidths=[None, 30, 30, 30, 30]

    return table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths)

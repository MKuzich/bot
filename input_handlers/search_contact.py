from input_error import input_error

@input_error
def search_contact(args, contacts):
    name = args[0]
    return contacts.search_by_any(name)

from errors import (
    NotValidPhoneNumber,
    NotValidDate,
    NameIsString,
    NoBirthday,
    NoContacts,
    NoBirthdays,
    EmailNotCorrect
)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except NotValidPhoneNumber:
            return "Phone number should contain only 10 digits."
        except NotValidDate:
            return "Date should be in format DD.MM.YYYY."
        except NameIsString:
            return "Name should contain only letters."
        except ValueError:
            return "Give me name and phone please."
        except NoBirthday:
            return "No birthday for this contact."
        except IndexError:
            return "Phone not found."
        except KeyError:
            return "Contact not found."
        except NoContacts: 
            return "No contacts in phonebook."
        except NoBirthdays:
            return "No birthdays in the next 7 days."
        except EmailNotCorrect:
            return "Email not correct."
        except:
            return "Something went wrong."
    return inner
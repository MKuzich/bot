from errors import (
    NotValidPhoneNumber,
    NotValidDate,
    NameIsString,
    NoBirthday,
    NoContacts,
    NoBirthdays,
    EmailNotCorrect,
    BuildingNumberNotCorrect,
    PostalCodeNotCorrect,
    CountryCodeNotCorrect
)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except NotValidPhoneNumber:
            return "Phone number should contain 10 or 12 digits."
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
        except BuildingNumberNotCorrect:
            return "Building number not correct."
        except PostalCodeNotCorrect:
            return "PostalCode not core=rect for this country"
        except CountryCodeNotCorrect:
            return "Inputed country code not correct or counry not found."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

from errors import (
    NotValidPhoneNumber,
    NotValidDate,
    NameIsString,
    NoBirthday,
    NoContacts,
    NoBirthdays,
    LimitSearchBirthdays,
    EmptyArgsBirthdays,
    EmptyArgsContact,
    EmailNotCorrect,
    BuildingNumberNotCorrect,
    PostalCodeNotCorrect,
    CountryCodeNotCorrect,
    NoteSearchError,
    NoteSearchTagError,
    NoteEmptyError
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
            return "\nNo contacts in phonebook.\n"
        except NoBirthdays:
            return "There are no birthdays in the specified period."
        except EmptyArgsBirthdays:
            return "\nYou must write a name, for example >>> show-birthday Siri\n"
        except EmptyArgsContact:
            return "\nYou should write a search element like >>> search-contact Siri\n"
        except LimitSearchBirthdays:
            return "Enter a date less than 365 days"
        except EmailNotCorrect:
            return "Email not correct."
        except BuildingNumberNotCorrect:
            return "Building number not correct."
        except PostalCodeNotCorrect:
            return "PostalCode not core=rect for this country"
        except CountryCodeNotCorrect:
            return "Inputed country code not correct or counry not found."
        except NoteSearchError:
            return "No notes found with those words."
        except NoteSearchTagError:
            return "No notes found with those tags."
        except NoteEmptyError:
            return "No notes found."
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

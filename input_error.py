from errors import (
    NotValidPhoneNumber,
    NotValidDate,
    NameIsString,
    NoBirthday,
    NoContacts,
    NoBirthdays,
    LimitSearchBirthdays,
    EmailNotCorrect,
    BuildingNumberNotCorrect,
    PostalCodeNotCorrect,
    CountryCodeNotCorrect,
    NoteSearchError,
    NoteSearchTagError,
    NoteEmptyError,
    NoteIdNotCorrect,
    NoteIdNotInList,
    NoteFormatError,
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
            return "There are no birthdays in the specified period."
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
        except NoteIdNotCorrect:
            return "Note ID should be an integer."
        except NoteIdNotInList:
            return "Note ID not in list."
        except NoteFormatError:
            return "Note format not correct. Usage: add-note <Title> <Description>"
        except Exception as e:
            return f"An error occurred: {e}"
    return inner

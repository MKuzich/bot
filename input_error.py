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
from constants import MESSAGES
from helpers.ui import get_red_html


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
        except NoBirthday:
            return "No birthday for this contact."
        except NoContacts:
            return "No contacts in phonebook."
        except NoBirthdays:
            return "There are no birthdays in the specified period."
        except LimitSearchBirthdays:
            return "Enter a date less than 365 days"
        except EmailNotCorrect:
            return get_red_html("Error: email format not correct")
        except BuildingNumberNotCorrect:
            return get_red_html("Error: Building number not correct.")
        except PostalCodeNotCorrect:
            return "PostalCode not core=rect for this country"
        except CountryCodeNotCorrect:
            return "Inputed country code not correct or counry not found."
        except NoteSearchError:
            return "No notes found with those words or numbers."
        except NoteSearchTagError:
            return "No notes found with those tags."
        except NoteEmptyError:
            return "No notes found."
        except Exception as e:
            return get_red_html(f"An error occurred: {e}")

    return inner

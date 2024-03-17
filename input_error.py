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
    NoteEmptyError,
    NoteValueArgsError,
    NoteIdNotCorrect,
    NoteIdNotInList,
    NoteFormatError,
    NoteIdAndTagNotEntered,
    TagNotEntered,
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
        except NoteValueArgsError:
            return "Usage: show-note <note_id>."
        except ValueError:
            return MESSAGES["not_correct_format"]
        except IndexError:
            return MESSAGES["not_found"]
        except KeyError:
            return MESSAGES["not_found"]
        except KeyboardInterrupt:
            return "Canceled!"
        except NoteIdNotCorrect:
            return "Note ID should be an integer."
        except NoteIdNotInList:
            return "Note ID not in list."
        except NoteFormatError:
            return "Note format not correct. Usage: add-note <Title> <Description>"
        except NoteIdAndTagNotEntered:
            return "Please enter note ID and minimum 1 tag."
        except TagNotEntered:
            return "Please enter minimum 1 tag."
        #except Exception as e:
        #    return get_red_html(f"An error occurred: {e}")

    return inner

from chandlerbot.errors import (
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
    AddressNotFound,
    NoteIdAndTagNotEntered,
    TagNotEntered,
    NoNotes
)
from chandlerbot.constants import MESSAGES
from chandlerbot.helpers.ui import get_red_html, get_bold_green_html


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except NotValidPhoneNumber:
            return get_red_html("Phone number should contain 10 or 12 digits.")
        except NotValidDate:
            return get_red_html("Date should be in format DD.MM.YYYY.")
        except NameIsString:
            return get_red_html("Name should contain only letters.")
        except NoBirthday:
            return get_bold_green_html("No birthday for this contact.")
        except NoContacts:
            return get_bold_green_html("No contacts in phonebook.")
        except NoNotes:
            return get_bold_green_html("No notes were found.")
        except NoBirthdays:
            return get_bold_green_html("There are no birthdays in the specified period.")
        except EmptyArgsBirthdays:
            return get_red_html("You must write a name in format: show-birthday &#10094; name &#10095;.")
        except EmptyArgsContact:
            return get_red_html("You should write a search element in format:> search-contact &#10094; name &#10095;.")
        except LimitSearchBirthdays:
            return get_red_html("Enter a date less than 365 days")
        except EmailNotCorrect:
            return get_red_html("Email format not correct")
        except BuildingNumberNotCorrect:
            return get_red_html("House number not correct.")
        except PostalCodeNotCorrect:
            return get_red_html("Postal code not correct for this country.")
        except CountryCodeNotCorrect:
            return get_red_html("Inputed country code not correct or counry not found.")
        except NoteSearchError:
            return get_bold_green_html("No notes found with those words or numbers.")
        except NoteSearchTagError:
            return get_bold_green_html("No notes found with those tags.")
        except NoteEmptyError:
            return get_bold_green_html("No notes found.")
        except NoteValueArgsError:
            return get_red_html("Usage: show-note &#10094; note_id &#10095;.")
        except ValueError:
            return MESSAGES["not_correct_format"]
        except IndexError:
            return MESSAGES["not_found"]
        except KeyError:
            return MESSAGES["not_found"]
        except KeyboardInterrupt:
            return get_bold_green_html("Canceled!")
        except NoteIdNotCorrect:
            return get_red_html("Note ID should be an integer.")
        except NoteIdNotInList:
            return get_red_html("Note ID not in list.")
        except NoteFormatError:
            return get_red_html("Note format not correct. Usage: add-note &#10094; title &#10095; &#10094; description &#10095;")
        except AddressNotFound:
            return get_bold_green_html("Address not found")
        except NoteIdAndTagNotEntered:
            return get_red_html("Please enter note ID and minimum 1 tag.")
        except TagNotEntered:
            return get_red_html("Please enter minimum 1 tag.")
        except Exception as e:
            return get_red_html(f"An error occurred: {e}")

    return inner

def load_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConnectionError:
            return None
        except Exception:
            return None
    return inner

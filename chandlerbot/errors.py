class NotValidPhoneNumber(ValueError):
    pass


class NotValidDate(ValueError):
    pass


class NameIsString(ValueError):
    pass


class NoContacts(Exception):
    pass

class NoNotes(Exception):
    pass


class NoBirthdays(Exception):
    """The date of birth search is limited to 365 days"""


class LimitSearchBirthdays(Exception):
    """The date of birth search is limited to 365 days"""

class EmptyArgsBirthdays(Exception):
    """You must write a name, for example >>> show-birthday Siri"""

class EmptyArgsContact(Exception):
    """You should write a search element like >>> show-contact Siri"""

class NoBirthday(KeyError):
    pass


class EmailNotCorrect(Exception):
    """Email not passed reqular expression"""


class BuildingNumberNotCorrect(Exception):
    """Buliding number not passed reqular expression"""


class StreetNotString(Exception):
    """Street not passed reqular expression"""


class CityNotString(Exception):
    """City code not passed reqular expression"""


class PostalCodeNotCorrect(Exception):
    """Postal code not passed reqular expression"""


class CountryCodeNotCorrect(Exception):
    """Given country code not correct"""


class NoteSearchError(Exception):
    """No notes found with those words or numbers"""


class NoteSearchTagError(Exception):
    """No notes found with those tags"""


class NoteEmptyError(Exception):
    """No tags entered for sorting"""

class NoteValueArgsError(Exception):
    """Usage: show-note <note_id>"""

class NoteIdNotCorrect(Exception):
    """Note id not correct"""


class NoteIdNotInList(Exception):
    """Note id not in list"""


class NoteFormatError(Exception):
    """Note format not correct"""

class AddressNotFound(Exception):
    """Address not found"""

class NoteIdAndTagNotEntered(Exception):
    """No id and tag entered"""


class TagNotEntered(Exception):
    """No tag entered"""

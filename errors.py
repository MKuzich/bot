class NotValidPhoneNumber(ValueError):
    pass

class NotValidDate(ValueError):
    pass

class NameIsString(ValueError):
    pass

class NoContacts(Exception):
    pass

class NoBirthdays(Exception):
    pass

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
    "No notes found with that word"
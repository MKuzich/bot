"""Function for search patters"""
from chandlerbot.constants import POSTAL_CODES_BY_COUNTRY

def get_pattern(name, country_code="UA"):
    """Return patterns by name or country"""
    if name == "POSTAL_CODE":
        if country_code in POSTAL_CODES_BY_COUNTRY:
            return POSTAL_CODES_BY_COUNTRY[country_code]
        return POSTAL_CODES_BY_COUNTRY[country_code]
    
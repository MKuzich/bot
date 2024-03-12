"""File for Address class"""
import re
from models.Field import Field
from errors import (
    BuildingNumberNotCorrect,
    StreetNotString,
    CityNotString,
    PostalCodeNotCorrect,
    CountryCodeNotCorrect
)
from helpers.patterns import get_pattern
from helpers.countries import get_country
from constants import BULDING_PATTER

class Street(Field):
    """Street class"""
    def __init__(self, name):
        if not isinstance(name, str):
            raise  StreetNotString
        super().__init__(name)

class BuldingNumber(Field):
    """Building number"""
    def __init__(self, build_number):
        build_number = str(build_number)
        if not re.match(BULDING_PATTER, build_number):
            raise BuildingNumberNotCorrect
        super().__init__(build_number)

class City(Field):
    """City"""
    def __init__(self, name):
        if not isinstance(name, str):
            raise  CityNotString
        super().__init__(name)

class CountryInfo(Field):
    """Country class"""
    def __init__(self, country):
        self.__country = country
        self.country = country
        super().__init__(country)

    @property
    def country(self):
        """Return country ISO code"""
        return self.__country.alpha_2

    @country.setter
    def country(self, country):
        """Setter for country"""
        found_country = get_country(country)
        if not found_country :
            raise CountryCodeNotCorrect
        self.__country = found_country

    @property
    def name(self):
        """Return country ISO name"""
        return self.__country.name


class PostalCode:
    """Postal code"""
    def __init__(self, code, country="UA") -> None:
        self.__code = None
        self.country = CountryInfo(country)
        self.code = code

    @property
    def code(self):
        """Return postal code"""
        return self.__code

    @code.setter
    def code(self, code):
        """Setter for postal code"""
        country_code = self.country.country
        postal_code_pattern = get_pattern("POSTAL_CODE", country_code)
        if not re.match(postal_code_pattern, str(code)):
            raise PostalCodeNotCorrect
        self.__code = str(code)


class Address:
    """Address for contact record"""
    def __init__(self, street, building_number,
                 city=None, postal_code=None, country="UA"):
        self.street = Street(street)
        self.building_number = BuldingNumber(building_number)
        self.city = City(city) if city else None
        self.postal_code = PostalCode(postal_code, country) if postal_code else None
        self.country = CountryInfo(country)

    def __str__(self):
        return f"{self.street}, {self.building_number}, {self.city}"

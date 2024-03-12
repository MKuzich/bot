"""Helpers for works with countries"""
import pycountry
from pycountry.db import Country

def search_country(country):
    """Search counnry by name or ISO code"""
    countries  = pycountry.countries.search_fuzzy(country)
    return  [c for c in countries if isinstance(c, Country)]

def get_country(country,):
    """get counnry by name or ISO code"""
    c = pycountry.countries.get(alpha_2=country)
    return c if c else pycountry.countries.get(name=country)
    
from collections import UserDict, defaultdict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        contact = self.data.get(name)
        if not contact:
            raise KeyError
        return contact

    def search_by_any(self, search_value):
        contacts = []
        for user in self.data.values():
            if search_value in user.name.value:
                contacts.append(user)
            elif user.email and search_value in user.email.value:
                contacts.append(user)
            elif any(search_value in phone.value for phone in user.phones):
                contacts.append(user)
            elif hasattr(user, 'birthday') and user.birthday and search_value in user.birthday.value.strftime('%d %B, %Y'):
                contacts.append(user)
        return contacts

    def delete(self, name):
        contact = self.data.pop(name, None)
        if not contact:
            raise KeyError
    
    def get_birthdays_per_week(self):
        today = datetime.now().date()
        birthdays = defaultdict(list)
        users = [{"name": user.name.value, "birthday": user.birthday.value} for user in self.data.values() if hasattr(user, 'birthday')]
        def sort_by_date(user):
            return user['birthday'].date()
        users.sort(key=sort_by_date)
        
        for user in users:
            name = user['name']
            birthday = user['birthday'].date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                if birthday_this_year.weekday() > 4: 
                    if today.weekday() != 0 and today.weekday() < 5:
                        birthdays['Monday'].append(name)
                else:
                    birthdays[birthday_this_year.strftime('%A')].append(name)
        return birthdays

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        #end_of_year = datetime(today.year, 12, 31).date()
        target_date = today + timedelta(days=int(days))
        birthdays = defaultdict(list)

        for user in self.data.values():
            if hasattr(user, 'birthday'):
                name = user.name.value
                phones = '; '.join(p.value for p in user.phones)
                email = user.email
                birthday = user.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if today <= birthday_this_year <= target_date:
                    day_of_week = birthday_this_year.strftime('(%A)')
                    formatted_date = birthday_this_year.strftime('%d %B, %Y')
                    birthdays[formatted_date].append((day_of_week, name, phones, email))

        return birthdays




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

    def find_by_name(self, search_value):
        contacts = []
        for user in self.data.values():
            if search_value in user.name.value.lower():
                contacts.append(user)

        return contacts

    def find_birthday_by_name(self, search_value):
        contacts = []
        for user in self.data.values():
            if search_value.lower() in user.name.value.lower():
                if hasattr(user, 'birthday'):
                    contacts.append(user)

        return contacts

    def find_address_by_name(self, search_value):
        contacts = []
        for user in self.data.values():
            if search_value.lower() == user.name.value.lower():
                address_str = (str(user.address).lower()
                           if hasattr(user, 'address') and user.address else "")

                if address_str:
                    contacts.append(user)

        return contacts

    def search_by_any(self, search_value):
        contacts = []
        search_value = search_value.lower()
        for user in self.data.values():
            birthday_str_formats = []
            if hasattr(user, 'birthday'):
                birthday_str_formats = self.birthdayStrFormats(user)

            address_str = (str(user.address).lower()
                           if hasattr(user, 'address') and user.address else "")

            if search_value in address_str:
                contacts.append(user)
            elif search_value in user.name.value.lower():
                contacts.append(user)
            elif user.email and search_value in user.email.value.lower():
                contacts.append(user)
            elif any(search_value in phone.value for phone in user.phones):
                contacts.append(user)
            elif (hasattr(user, 'birthday') and user.birthday and search_value
                  in birthday_str_formats):
                contacts.append(user)

        return contacts

    def birthdayStrFormats(self, user):
        return [
            user.birthday.value.strftime('%d.%m.%Y').lower(),  # 22.07.1983
            user.birthday.value.strftime('%d').lower(),        # 22
            user.birthday.value.strftime('%m').lower(),        # 07
            user.birthday.value.strftime('%m').lstrip('0').lower(),       # 7
            user.birthday.value.strftime('%Y').lower(),        # 1983
            user.birthday.value.strftime('%d %B').lower(),     # 22 July
            user.birthday.value.strftime('%B').lower(),        # July
            user.birthday.value.strftime('%d.%m').lower(),     # 22.07
        ]

    def delete(self, name):
        contact = self.data.pop(name, None)
        if not contact:
            raise KeyError

    def get_count_birthdays_per_week(self):
        today = datetime.now().date()
        target_date = today + timedelta(days=7)
        count = 0
        
        for user in self.data.values():
            if hasattr(user, 'birthday'):
                # Переконуємося, що працюємо з датою, а не з datetime
                birthday_date = user.birthday.value.date() if isinstance(user.birthday.value, datetime) else user.birthday.value
                birthday_this_year = birthday_date.replace(year=today.year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                
                if today <= birthday_this_year <= target_date:
                    count += 1

        return count

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

            if delta_days < 300:
                if birthday_this_year.weekday() > 4: 
                    if today.weekday() != 0 and today.weekday() < 5:
                        birthdays['Monday'].append(name)
                else:
                    birthdays[birthday_this_year.strftime('%A')].append(name)
        return birthdays

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        #end_of_year = datetime(today.year, 12, 31).date()
        target_date = today + timedelta(days=days)
        birthdays = defaultdict(list)

        for user in self.data.values():
            if hasattr(user, 'birthday'):
                name = user.name.value
                phones = '; '.join(p.value for p in user.phones)
                email = user.email
                address = user.address
                birthday = user.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if today <= birthday_this_year <= target_date:
                    day_of_week = birthday_this_year.strftime('(%A)')
                    formatted_date = birthday_this_year.strftime('%d %B, %Y')
                    birthdays[formatted_date].append((day_of_week, name, phones, email, address))

        return birthdays

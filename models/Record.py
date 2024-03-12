from models.Name import Name
from models.Phone import Phone
from models.Birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_idx(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                return i
        raise IndexError

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        idx = self.find_idx(phone)
        self.phones.pop(idx)

    def edit_phone(self, phone, new_phone):
        idx = self.find_idx(phone)
        self.phones[idx].value = new_phone

    def find_phone(self, phone):
        idx = self.find_idx(phone)
        return self.phones[idx]
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{', birthday: ' + self.birthday.value.strftime('%d %B, %Y') if hasattr(self, 'birthday') else ''}"

from models import Name, Phone, Birthday, Email, Address

class Record:
    def __init__(self, name, email=None, address=None):
        self.name = Name(name)
        self.phones = []
        self.email = Email(email) if email else None
        self.address = address

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

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, *args):
        self.address = Address(*args)

    def remove_email(self, ):
        self.email = None

    def remove_address(self, ):
        self.address = None

    def remove_birthday(self, ):
        del self.birthday

    def get_birthday(self):
        if self.birthday:
            return self.birthday.value.strftime("%d.%m.%Y")

    def __str__(self):
        email = self.email if self.email else None
        return f"Email {email} Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, Address: {self.address}{', birthday: ' + self.birthday.value.strftime('%d %B, %Y') if hasattr(self, 'birthday') else ''}"

    def __repr__(self):
        return self.__str__()
    
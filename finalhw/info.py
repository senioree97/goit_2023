import time
from datetime import datetime
from collections import UserDict
from termcolor import colored

today = datetime.today()

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __get__(self):
        return self.value
    
    def __set__(self, new_value):
        self.value = new_value


class Name(Field):
    pass

class Birthday(Field):
    def __init__(self, value):
        if not self.is_valid_birthday(value):
            raise ValueError("Not valid birthday")
        super().__init__(value)
        

    def is_valid_birthday(self, value):
        try:
            valid_date = time.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def __set__(self, new_value):
        if not self.is_valid_birthday(new_value):
            raise ValueError("Not valid birthday")
        self.value = new_value


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Not valid phone")
        super().__init__(value)

    def is_valid_phone(self, value):
        return len(value) == 10 and int(value.isdigit())
    
    def __set__(self, new_value):
        if not self.is_valid_phone(new_value):
            raise ValueError("Not valid phone")
        self.value = new_value

    def __str__(self):
        return self.value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ""

    def days_to_birthday(self):
        if self.birthday:
            birth_date = datetime.strptime(self.birthday, '%Y-%m-%d')
            next_birthday = birth_date.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

    def add_birthday(self, birthday):
        self.birthday = birthday

    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                found = True
        if not found:
            raise ValueError("Phone not found")

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
        
    def get_phones(self):
        return [p.value for p in self.phones]
        
    def __str__(self):
        if self.birthday:
            return colored(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}!", "yellow")
        else:
            return colored(f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}!", "yellow")
    
class AddressBook(UserDict):

    def iterator(self, N=1):
        records = list(self.data.values())
        current_index = 0
        while current_index < len(records):
            yield records[current_index:current_index + N]
            current_index += N


    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
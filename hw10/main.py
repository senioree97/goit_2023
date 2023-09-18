from collections import UserDict
from termcolor import colored
import time


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Not valid phone")
        super().__init__(value)

    def is_valid_phone(self, value):
        return len(value) == 10 and value.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if not isinstance(phone, Phone):
            phone = Phone(phone)
        self.phones.append(phone)

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
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    
class AddressBook(UserDict):
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



known_commands = ("add", "change", "phone", "show","hello")
exit_commands = ("good bye", "close", "exit", ".")

def input_error(func):
        def inner(*args):
            try:
                try:
                    try:
                        return func(*args)
                    except IndexError:
                        print(colored("Index error", "red"))
                except ValueError:
                    print(colored("Value Error", "red"))             
            except KeyError:
                print(colored("Key error", "red"))
        return inner


def main():
    book = AddressBook()

    
    @input_error
    def add(name, *phones):
        contact = book.find(name)
        if contact is None:
            contact = Record(name)
            book.add_record(contact)

        for phone in phones:
            sanitized_phone = sanitize_phone_number(phone)
            if sanitized_phone.isdigit():
                contact.add_phone(sanitized_phone)
            else:
                return colored(f"Phone {sanitized_phone} is not valid and was not added to {name}", "red")
        
        return colored(f"Phone numbers were successfully added to {name}:\n{name}     {', '.join(phones)}", "green")



    @input_error
    def change(name, old_phone, phone):
        if name in book.data:
            record = book.data[name]
            if old_phone in record.get_phones():
                record.edit_phone(old_phone, phone)
                return colored(f"Contact number of {name} was successfully changed! New data:\n{name}     {phone}", "green")
            else:
                return colored("There is no number like this in that contact", "red")
        else:
            return colored("There is no contact with this name!", "red")


    @input_error
    def phone(name):
        if name in book.data:
            record = book.data[name]
            return colored(f"{name} was found in your contacts! Phones - {'; '.join(record.get_phones())}", "green")
        else:
            return colored("There is no contact with this name!", "red")

    @input_error
    def showall():
        print("{:>10}|{:^15}".format("NAME", "PHONES"))
        for record in book.values():
            print("{:>10}|{:<15}".format(record.name.value, '; '.join(record.get_phones())))


    @input_error
    def sanitize_phone_number(phone):
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone

    while True:
        input_text = input("⬇ Type your command below! ⬇ \n")
        input_command = (input_text.split()[0].lower())
        input_data = input_text.split()
        if input_command in exit_commands:
            print(colored("♡ Goodbye! ♡", "magenta"))
            break
        elif input_command in known_commands:
            if input_command == "hello":
                print(colored("♡ How can I help you, my dear? ♡", "magenta"))
            elif input_command == "add":
                try:
                    print(add(input_data[1], input_data[2]))
                except IndexError:
                    print(colored("You have to put name and phone after add. Example: \nadd -name -phone", "red"))
            elif input_command == "change":
                print(change(input_data[1], input_data[2], input_data[3]))
            elif input_command == "phone":
                print(phone(input_data[1]))
            elif "show all" in input_text:
                showall()
        else:
            print(colored("'◠' I don't know this command '◠'", "red"))

if __name__ == "__main__":
    main()

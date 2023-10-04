from info import *
from termcolor import colored
import pickle

class Bot:
    def __init__(self) -> None:
        self.book = AddressBook()

    def save(self, file_name):
        with open(file_name + ".bin", "wb") as file:
            pickle.dump(self.book, file)
        return colored("Book was succesfully saved.", "green")


    def load(self, file_name):
        with open(file_name + ".bin", "rb") as file:
            self.book = pickle.load(file)
        return self.book
    
    def search(self, search_For = ""):
        found = list()
        found_num = 0
        for i in self.book:
            if self.book[i].name.value.lower().startswith(search_For.lower()):
                found_num += 1
                
                found.append(self.book[i])
            for _ in [p.value for p in self.book[i].phones]:
                if _.startswith(search_For):
                    found_num += 1
                    found.append(self.book[i])
        if found_num:
            print(colored(f"Were(was) found {found_num} contact(s) with your pattern!", "green"))            
            print(colored("Here are the contacts we found: ", "green"))
            for j in found:
                print(j)
        else:
            print(colored("No contacts were found :(, try using another pattern", "red"))

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
        
    @input_error
    def add(self, name, *phones):
        contact = self.book.find(name)
        if contact is None:
            contact = Record(name)
            self.book.add_record(contact)

        for phone in phones:
            sanitized_phone = self.sanitize_phone_number(phone)
            if sanitized_phone.isdigit():
                contact.add_phone(sanitized_phone)
            else:
                return colored(f"Phone {sanitized_phone} is not valid and was not added to {name}", "red")
        
        return colored(f"Phone numbers were successfully added to {name}:\n{name}     {', '.join(phones)}", "green")



    @input_error
    def change(self, name, old_phone, phone):
        if name in self.book.data:
            record = self.book.data[name]
            if old_phone in record.get_phones():
                record.edit_phone(old_phone, phone)
                return colored(f"Contact number of {name} was successfully changed! New data:\n{name}     {phone}", "green")
            else:
                return colored("There is no number like this in that contact", "red")
        else:
            return colored("There is no contact with this name!", "red")


    @input_error
    def phone(self, name):
        if name in self.book.data:
            record = self.book.data[name]
            return colored(f"{name} was found in your contacts! Phones - {'; '.join(record.get_phones())}", "green")
        else:
            return colored("There is no contact with this name!", "red")

    @input_error
    def showall(self):
        if not len(self.book) == 0:
            for record in self.book.values():
                print(record)
        else:
            print(colored("Your AddressBook is empty!", "red"))



    @input_error
    def sanitize_phone_number(self, phone):
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone
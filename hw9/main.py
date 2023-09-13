from termcolor import colored
import time

known_commands = ("add", "change", "phone", "show","hello")
exit_commands = ("good bye", "close", "exit", ".")


def main():
    contacts={}


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
    def add(name, phone):
        if sanitize_phone_number(phone).isdigit():
            contacts[name] = sanitize_phone_number(phone)
            return (colored(f"Contact was succesfully added to your contacts! \n{name}     {phone}", "green"))
        else:
            return (colored("Try again using a valid nunber.", "red"))


    @input_error
    def change(name, phone):
        if name in contacts:
            contacts[name]=phone
            return (colored(f"Contact number of {name} was succesfully changed! New data: \n{name}     {phone}", "green"))
        else:
            return (colored("There is no contact with this name!", "red"))


    @input_error
    def phone(name):
        if name in contacts:
            return (colored(f"{name} was found in your contacts! Phone - {contacts.get(name)}","green"))
        else:
            return (colored("There is no contact with this name!", "red"))
        

    @input_error
    def showall():
        print("|{:>10}|{:>15}|".format("NAME","PHONE"))
        for name,phone in contacts.items():
            print("|{:>10}|{:>15}|".format(name,phone))

    
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
        print("Processing...\n")
        time.sleep(2)
        input_command=(input_text.split()[0].lower())
        input_data=input_text.split()
        if input_command in exit_commands:
            print(colored("♡ Good bye! ♡", "magenta"))
            break
        elif input_command in known_commands:
            if input_command=="hello":
                print(colored("♡ How can I help you, my dear? ♡", "magenta"))
            elif input_command=="add":
                try:
                    print(add(input_data[1],input_data[2]))
                except IndexError:
                    print(colored("you have to put name and phone after add. Example: \nadd -name -phone","red"))
            elif input_command=="change":
                print(change(input_data[1],input_data[2]))
            elif input_command=="phone":
                print(phone(input_data[1]))
            elif "show all" in input_text:
                showall()
        else:
            print(colored("'◠' I dont know this command '◠'", "red"))
    

if __name__ == "__main__":
    main()
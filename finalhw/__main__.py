from termcolor import colored
from info import *
from Bot import Bot

Bot = Bot()

known_commands = ("add", "change", "phone", "show", "hello", "help", "save", "load", "search", "birthday")
exit_commands = ("goodbye", "close", "exit", ".")
commands = known_commands + exit_commands

def main():
    try:
        Bot.load("auto_save")
    except FileNotFoundError:
        ...

    while True:
        input_text = input("⬇ Type your command below! help for commands ⬇ \n")
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
                    print(Bot.add(input_data[1], input_data[2]))
                except IndexError:
                    print(colored("Try using add like that: add [name] [phone]", "red"))
            elif input_command == "change":
                try:
                    print(Bot.change(input_data[1], input_data[2], input_data[3]))
                except IndexError:
                    print(colored("Try using change like that: change [name] [previous number] [new number]", "red"))
            elif input_command == "phone":
                try:
                    print(Bot.phone(input_data[1]))
                except IndexError:
                    print(colored("Try using phone like that: phone [name]", "red"))
            elif input_command == "help":
                for command in commands:
                    print("|{:^20}|".format(command))
            elif "show all" in input_text:
                Bot.showall()
            elif input_command == "save":
                print(Bot.save("auto_save"))
            elif input_command == "load":
                Bot.load("auto_save")
                print("Book was successfully loaded")
            elif input_command == "search":
                try:
                    Bot.search(input_data[1])
                except IndexError:
                    print(colored("Try using search like that: search [what to look for number or name]", "red"))
        else:
            print(colored("'◠' I don't know this command '◠'", "red"))



if __name__ == "__main__":
    # book = AddressBook()
    
    # p1 = Record("Anton")
    # p2 = Record("Gennadiy")

    # p1.add_phone("3866982045")
    # p2.add_phone("3334534045")

    # p4 = Record("Anton2")
    # p3 = Record("Gennadiy2")

    # p3.add_phone("3863242304")
    # p4.add_phone("3332432404")


    # p1.add_birthday("2021-07-06")
    # print(f'p1s birthday is in {p1.days_to_birthday()} days')

    # book.add_record(p1)
    # book.add_record(p2)
    # book.add_record(p3)
    # book.add_record(p4)


    # for page_number, chunks in enumerate(book.iterator(N=2), start=1):
    #     print(f"Page {page_number}\n")
    #     for record in chunks:
    #         print(record)

    main()

    

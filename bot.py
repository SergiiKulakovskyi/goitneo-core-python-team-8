from datetime import datetime

from classes.record import Record
from classes.address_book import AddressBook


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone(10 digits) please."
        except IndexError:
            return "Give me name please."

    return inner


@input_error
def add_contact(args, book):
    name, phone = args
    if name not in book.data:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    else:
        return "Contact with the same name already exists."


@input_error
def change_contact(args, book):
    name, new_phone = args
    if name in book.data:
        record = book.find(name)
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, book):
    name = args[0]
    if name in book.data:
        record = book.find(name)
        return record.phones[0].value
    else:
        return "Contact not found."


@input_error
def show_all(book):
    contacts = []
    for record in book.data.values():
        contacts.append(f"{record.name.value}: {record.phones[0].value}")
    return "\n".join(contacts)


def add_birthday(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Provide name and birthday."

    name, birthday = args
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        return "Incorrect date format. Should be 'DD.MM.YYYY'."

    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact {name} not found."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday}."
    elif record and not record.birthday:
        return f"{name} has no birthday set."
    else:
        return f"Contact {name} not found."


def birthdays(book):
    upcoming_birthdays = book.get_birthdays_per_week()
    if upcoming_birthdays:
        return upcoming_birthdays
    else:
        return "No upcoming birthdays in the next week."


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            print("Please, enter your command")
            continue

        command, *args = parse_input(user_input)

        # contacts
        if command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))

        # birthdays
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))

        # common
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

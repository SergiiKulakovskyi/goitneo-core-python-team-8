from handlers.add_contact import add_contact
from handlers.change_contact import change_contact
from handlers.show_phone import show_phone
from handlers.show_all import show_all
from handlers.add_birthday import add_birthday
from handlers.show_birthday import show_birthday
from handlers.birthdays import birthdays
from utils.storage import save_to_file, load_from_file


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    filename = 'address_book.pkl'
    book = load_from_file(filename)

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
            save_to_file(book, filename)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

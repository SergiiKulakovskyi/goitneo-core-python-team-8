from handlers.add_contact import add_contact
from handlers.change_contact import change_contact
from handlers.show_phone import show_phone
from handlers.show_all import show_all
from handlers.add_birthday import add_birthday
from handlers.show_birthday import show_birthday
from handlers.birthdays import birthdays
from utils.storage import save_to_file, load_from_file
from utils.args_parser import ArgsParser
from argparse import Namespace

from classes.note_book import NoteBook
from handlers.add_note import add_note
from handlers.all_notes import all_notes
from handlers.find_notes import find_notes
from handlers.edit_note import edit_note
from handlers.delete_note import delete_note
from handlers.add_note_tag import add_note_tag
from handlers.remove_note_tag import remove_note_tag


def main():
    filename = 'address_book.pkl'
    book = load_from_file(filename)
    note_book = NoteBook()

    args_parser = ArgsParser()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            print("Please, enter your command")
            continue

        args: Namespace = args_parser.parse(user_input)
        command = args.command

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

        # notes
        elif command == "add-note":
            print(add_note(args, note_book))
        elif command == "find-notes":
            print(find_notes(args, note_book))
        elif command == "all-notes":
            print(all_notes(note_book))
        elif command == "edit-note":
            print(edit_note(args, note_book))
        elif command == "delete-note":
            print(delete_note(args, note_book))
        elif command == "add-note-tag":
            print(add_note_tag(args, note_book))
        elif command == "remove-note-tag":
            print(remove_note_tag(args, note_book))

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

import pickle
from classes.address_book import AddressBook
from handlers.add_contact import add_contact
from handlers.change_contact import change_contact
from handlers.show_phone import show_phone
from handlers.show_all import show_all
from handlers.add_birthday import add_birthday
from handlers.show_birthday import show_birthday
from handlers.birthdays import birthdays
from utils.storage import save_to_file, load_from_file
from utils.args_parser import ArgsParser
from utils.similar_commands_analysis import find_most_similar_command
from argparse import Namespace

from classes.note_book import NoteBook
from handlers.add_note import add_note
from handlers.all_notes import all_notes
from handlers.find_notes import find_notes
from handlers.edit_note import edit_note
from handlers.delete_note import delete_note
from handlers.add_note_tag import add_note_tag
from handlers.remove_note_tag import remove_note_tag
from handlers.search_notes_by_tags import search_notes_by_tags

def main():
    address_book_filename = 'address_book.pkl'
    notes_filename = 'notes.pkl'

    book = load_from_file(address_book_filename, AddressBook)
    note_book = load_from_file(notes_filename, NoteBook)

    args_parser = ArgsParser()
    available_commands = args_parser.get_available_commands()

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
            print(birthdays(args.days, book))

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
        elif command == "search-notes-by-tags":
            print(search_notes_by_tags(args, note_book))

        # common
        elif command in ["close", "exit"]:
            save_to_file(book, address_book_filename)
            save_to_file(note_book, notes_filename)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            pass  # it's already handled by argparse
        else:
            similar_command = find_most_similar_command(user_input.split()[0], available_commands)
            print("Unknown command. See --help for available commands.")
            
            if similar_command:
                print(f"The most similar command is '{similar_command}'")
                

if __name__ == "__main__":
    main()

import shlex
import argparse


class ArgsParser:
    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser(
            description="Address Book and Notes bote", exit_on_error=False)

        subparsers = self._parser.add_subparsers(
            title="Commands", dest="command")

        add_contact_parser = subparsers.add_parser(
            "add", help="Add new contact to address book")
        add_contact_parser.add_argument(
            "-n", "--name", type=str, help="Contact name", required=True)
        add_contact_parser.add_argument(
            "-p", "--phone", type=str, help="Contact phone")
        add_contact_parser.add_argument(
            "-a", "--address", type=str, help="Contact address")
        add_contact_parser.add_argument(
            "-e", "--email", type=str, help="Contact email")
        add_contact_parser.add_argument(
            "-b", "--birthday", type=str, help="Contact birthday in format DD.MM.YYYY")

        change_contact_parser = subparsers.add_parser(
            "change", help="Change existing contact in address book")
        change_contact_parser.add_argument(
            "-n", "--name", type=str, help="Contact name", required=True)
        change_contact_parser.add_argument(
            "-p", "--phone", type=str, help="New contact phone")
        change_contact_parser.add_argument(
            "-a", "--address", type=str, help="New contact address")
        change_contact_parser.add_argument(
            "-e", "--email", type=str, help="New contact email")
        change_contact_parser.add_argument(
            "-b", "--birthday", type=str, help="New contact birthday in format DD.MM.YYYY")

        search_contacts_parser = subparsers.add_parser(
            "search-contacts", help="Search for contacts in address book by specific criteria")

        search_contacts_parser.add_argument("-c", "--criteria", type=str, nargs='?', default="name", choices=[
                                            "name", "phone", "address", "email", "birthday"], help="The criteria to search by")
        search_contacts_parser.add_argument(
            "text", type=ArgsParser._search_text_length, help="The text to search for")

        subparsers.add_parser(
            "all", help="Show all existing contacts in address book")
        subparsers.add_parser("close", help="Close the bot")
        subparsers.add_parser("exit", help="Close the bot")
        subparsers.add_parser("hello", help="Show greeting message")

        # birthdays
        birthdays_parser = subparsers.add_parser(
            "birthdays", help="Show all contacts with birthdays in a specified number of days (1 - 180)")
        birthdays_parser.add_argument(
            "days", type=int, nargs='?', default=7,
            help="Number of days from today to check for upcoming birthdays")

        # add-note
        add_note_parser = subparsers.add_parser(
            "add-note", help="Creates a new note")
        add_note_parser.add_argument(
            "text", type=str, help="The text of the note.")

        # find-notes
        find_notes_parser = subparsers.add_parser(
            "find-notes", help="Searches for notes based on specific criteria, such as the note content or tags")
        find_notes_parser.add_argument(
            "text", type=str, help="The text to search for in the notes.")

        # all-notes
        subparsers.add_parser("all-notes", help="Lists all of the notes")

        # edit-note
        edit_note_parser = subparsers.add_parser(
            "edit-note", help="Edits an existing note")
        edit_note_parser.add_argument(
            "id", type=int, help="The ID of the note to edit.")
        edit_note_parser.add_argument(
            "text", type=str, help="The new text for the note.")

        # delete-note
        delete_note_parser = subparsers.add_parser(
            "delete-note", help="Deletes an existing note")
        delete_note_parser.add_argument(
            "id", type=int, help="The ID of the note to delete.")

        # add-note-tag
        add_note_tag_parser = subparsers.add_parser(
            "add-note-tag", help="Adds a tag to an existing note")
        add_note_tag_parser.add_argument(
            "id", type=int, help="The ID of the note to add the tag to.")
        add_note_tag_parser.add_argument(
            "tag", type=str, help="The tag to add to the note.")

        # remove-note-tag
        remove_note_tag_parser = subparsers.add_parser(
            "remove-note-tag", help="Removes a tag from an existing note")
        remove_note_tag_parser.add_argument(
            "id", type=int, help="The ID of the note to remove the tag from.")
        remove_note_tag_parser.add_argument(
            "tag", type=str, help="The tag to remove from the note.")

        # search-notes-by-tags
        search_notes_by_tags_parser = subparsers.add_parser(
            "search-notes-by-tags", help="Search notes by tags.")
        search_notes_by_tags_parser.add_argument(
            "tags", nargs='+', help="The tags to search for.")

    def parse(self, user_input):
        args = shlex.split(user_input)
        return self._parser.parse_args(args)

    def get_available_commands(self):
        subparsers = self._parser._subparsers._group_actions
        available_commands = [parser.choices.keys()
                              for parser in subparsers if hasattr(parser, 'choices')]
        return [command for commands in available_commands for command in commands]

    @staticmethod
    def _search_text_length(value):
        if len(value) < 2:
            raise argparse.ArgumentTypeError("The 'text' argument must be at least 2 characters long.")
        return value
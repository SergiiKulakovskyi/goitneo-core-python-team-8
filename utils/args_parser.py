import shlex
import argparse
from datetime import datetime, date

class ArgsParser:
    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser(description="Address Book and Notes bote")
        subparsers = self._parser.add_subparsers(title="Commands", dest="command")

        add_contact_parser = subparsers.add_parser("add", help="Add new contact to address book")
        add_contact_parser.add_argument("-n", "--name", type=str, help="Contact name", required=True)
        add_contact_parser.add_argument("-p", "--phone", type=str, help="Contact phone")
        add_contact_parser.add_argument("-a", "--address", type=str, help="Contact address")
        add_contact_parser.add_argument("-e", "--email", type=str, help="Contact email")
        add_contact_parser.add_argument("-b", "--birthday", type=ArgsParser.__date_parser, help="Contact birthday in format DD.MM.YYYY")

        change_contact_parser = subparsers.add_parser("change", help="Change existing contact in address book")
        change_contact_parser.add_argument("-n", "--name", type=str, help="Contact name", required=True)
        change_contact_parser.add_argument("-p", "--phone", type=str, help="New contact phone")
        change_contact_parser.add_argument("-a", "--address", type=str, help="New contact address")
        change_contact_parser.add_argument("-e", "--email", type=str, help="New contact email")
        change_contact_parser.add_argument("-b", "--birthday", type=ArgsParser.__date_parser, help="New contact birthday in format DD.MM.YYYY")

        subparsers.add_parser("all", help="Show all existing contacts in address book")
        subparsers.add_parser("birthdays", help="Show all contacts with birthdays in next 7 days")
        subparsers.add_parser("close", help="Close the bot")
        subparsers.add_parser("exit", help="Close the bot")
        subparsers.add_parser("hello", help="Show greeting message")

    def parse(self, user_input):
        try:
            args = shlex.split(user_input)
            return self._parser.parse_args(args)
        except:
            return argparse.Namespace(command=None)
    
    @staticmethod
    def __date_parser(date_string: str) -> date:
        return datetime.strptime(date_string, "%d.%m.%Y").date()

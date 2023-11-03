from classes.note_book import Note
from classes.record import Record
from tabulate import tabulate
from decorators.input_error import input_error


@input_error()
def display_contacts(contacts: list[Record]) -> str:
    if (not len(contacts)):
        raise ValueError('No contacts were found')

    headers = ["Name", "Email", "Phone", "Birthday", "Address"]
    rows = [[getattr(record, field, '') for field in [
        'name', 'email', 'phone', 'birthday', 'address']] for record in contacts]
    return tabulate(rows, headers=headers, tablefmt="grid")


@input_error()
def display_notes(notes: list[Note]) -> str:
    if (not len(notes)):
        raise ValueError('No notes were found')

    headers = ["ID", "Tags", "Text"]
    rows = []
    for note in notes:
        rows.append([note.id, ', '.join(note.tags), note.text])
    return tabulate(rows, headers=headers, tablefmt="grid")

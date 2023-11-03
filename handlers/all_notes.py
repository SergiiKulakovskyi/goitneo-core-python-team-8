from classes.note_book import NoteBook
from utils.representation import display_notes


def all_notes(note_book: NoteBook):
    return display_notes(note_book.notes)

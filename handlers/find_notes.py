from decorators.input_error import input_error
from utils.representation import display_notes


@input_error(message='Type at least two characters to search the note')
def find_notes(args, note_book):
    try:
        search_text = getattr(args, "text").strip()
        if (len(search_text) >= 2):
            notes = note_book.find_notes(search_text)

            return display_notes(notes)
        raise
    except:
        raise ValueError

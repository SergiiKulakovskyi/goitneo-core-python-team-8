from decorators.input_error import input_error


@input_error(message='You must enter text for a note')
def add_note(args, note_book):
    try:
        text = getattr(args, "text").strip()
        id = note_book.add_note(text)
        return f"Note added with ID #{id}"
    except:
        raise ValueError

from decorators.note_error import note_error


@note_error(message='You must enter the ID of the note and the text to edit it')
def edit_note(args, note_book):
    try:
        id = int(getattr(args, "id"))
        text = getattr(args, "text")
    except:
        raise ValueError
    note_book.edit_note(id, text)
    return f"Note with ID #{id} has been changed"

from decorators.note_error import note_error


@note_error(message='You must enter the ID of the note to delete')
def delete_note(args, note_book):
    try:
        id = int(getattr(args, "id"))
    except:
        raise ValueError
    note_book.delete_note(id)
    return f"Note with ID #{id} has been deleted"

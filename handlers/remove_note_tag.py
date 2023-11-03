from decorators.input_error import input_error


@input_error(message='You must enter the ID of the note and the tag name to remove it')
def remove_note_tag(args, note_book):
    try:
        id = int(getattr(args, "id"))
        text = getattr(args, "tag").strip()
    except:
        raise ValueError
    note_book.remove_note_tag(id, text)
    return f'Tag "{text}" was removed from the note with ID #{id}'

from decorators.note_error import note_error


@note_error(message='You must enter the ID of the note and the tag name to tag it')
def add_note_tag(args, note_book):
    try:
        id = int(getattr(args, "id"))
        text = getattr(args, "tag").strip()
    except:
        raise ValueError
    note_book.add_note_tag(id, text)
    return f'Tag "{text}" was added to the note with ID #{id}'

from decorators.note_error import note_error


@note_error(message='Type at least two characters to search the note')
def find_notes(args, note_book):
    try:
        search_text = getattr(args, "text").strip()
        if (len(search_text) >= 2):
            notes = note_book.find_notes(search_text)

            result = []
            for note in notes:
                result.append(str(note))

            if len(result) == 0:
                return 'No notes were found'

            return '\n'.join(result)
        raise
    except:
        raise ValueError

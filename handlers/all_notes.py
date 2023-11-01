def all_notes(note_book):
    result = []
    for note in note_book.notes:
        result.append(str(note))

    if len(result) == 0:
        return 'No notes were found'

    return '\n'.join(result)

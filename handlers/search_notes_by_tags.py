from decorators.note_error import note_error


@note_error(message='No notes found with the specified tags')
def search_notes_by_tags(args, note_book):
    groups = note_book.search_by_tags(getattr(args, "tags"))

    if (not len(groups)):
        raise ValueError

    result = ''
    for key in sorted(groups):
        result += f'TAG: {key} \n'
        for note in groups[key]:
            result += f'  {note} \n'
    return result

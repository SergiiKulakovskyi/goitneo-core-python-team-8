from tabulate import tabulate
from decorators.input_error import input_error


@input_error()
def search_notes_by_tags(args, note_book):
    groups = note_book.search_by_tags(getattr(args, "tags"))

    if (not len(groups)):
        raise ValueError('No notes found with the specified tags')

    result = ''

    headers = ["ID", "Tag", "Text"]
    for key in sorted(groups):
        result += f'\nNotes with tag "{key}" \n'
        rows = []
        for note in groups[key]:
            rows.append([note.id, ', '.join(note.tags), note.text])
        result += tabulate(rows, headers=headers, tablefmt="grid") + '\n'
    return result

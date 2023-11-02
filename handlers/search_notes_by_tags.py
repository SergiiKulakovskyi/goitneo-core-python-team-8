from tabulate import tabulate
from decorators.note_error import note_error


@note_error(message='No notes found with the specified tags')
def search_notes_by_tags(args, note_book):
    groups = note_book.search_by_tags(getattr(args, "tags"))

    if (not len(groups)):
        raise ValueError

    headers = ["ID", "Tag", "Text"]
    for key in sorted(groups):
        print(f'Notes with tag {key}')
        rows = []
        for note in groups[key]:
            rows.append([note.id, ', '.join(note.tags), note.text])
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    return 'result'

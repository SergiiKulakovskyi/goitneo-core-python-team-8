import re


class Note:
    def __init__(self, id, text, tags=[]):
        self.id = id
        self.text = text
        self.tags = tags

    def __str__(self):
        tags_list = ''
        if len(self.tags) > 0:
            tags_list = f'(tags: {", ".join(sorted(self.tags))})'
        return f'Note #{self.id}: {self.text} {tags_list}'


class NoteBook:
    def __init__(self):
        self.notes = []

    def __find_largest_id(self):
        largest_numeric_id = 0
        for note in self.notes:
            if note.id > largest_numeric_id:
                largest_numeric_id = note.id
        return largest_numeric_id

    def add_note(self, text, tags=[]):
        note = Note(self.__find_largest_id() + 1, text, [])
        note.tags = tags
        self.notes.append(note)
        return note.id

    def find_notes(self, search_text):
        found_notes = []
        for note in self.notes:
            if re.search(search_text, note.text):
                found_notes.append(note)
        return found_notes

    def edit_note(self, id, text):
        for note in self.notes:
            if note.id == id:
                note.text = text
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def delete_note(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def add_note_tag(self, id, tag):
        for note in self.notes:
            if note.id == id:
                if tag in note.tags:
                    raise ValueError(
                        f"Tag '{tag}' already exists for this note")
                note.tags.append(tag)
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def remove_note_tag(self, id, tag):
        for note in self.notes:
            if note.id == id:
                try:
                    note.tags.remove(tag)
                except:
                    raise IndexError(
                        f"Note with ID {id} does not have the specified tag")
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def search_by_tags(self, tags):
        grouped_notes = {}

        for note in self.notes:
            for tag in note.tags:
                if tag in tags:
                    if tag not in grouped_notes:
                        grouped_notes[tag] = []
                    grouped_notes[tag].append(note)

        for tag, notes in grouped_notes.items():
            notes.sort(key=lambda note: "|".join(sorted(note.tags)))
            notes.sort(key=lambda note: len(note.tags), reverse=True)

        return grouped_notes

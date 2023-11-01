import re


class Note:
    def __init__(self, id, text, tags=[]):
        self.id = id
        self.text = text
        self.tags = tags

    def __str__(self):
        tags_list = ''
        if len(self.tags) > 0:
            tags_list = f'(tags: {", ".join(self.tags)})'
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

    def add_note(self, text):
        note = Note(self.__find_largest_id() + 1, text, [])
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
                note.tags.append(tag)
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def remove_note_tag(self, id, tag):
        for note in self.notes:
            if note.id == id:
                note.tags.remove(tag)
                return
        raise IndexError(f"Note with ID {id} does not exist")

    def find_note_by_tag(self, tag):
        # TODO
        raise IndexError(f"Notes with tag {tag} do not exist")

    def save(self):
        # TODO
        pass

    def load(self):
        # TODO
        pass

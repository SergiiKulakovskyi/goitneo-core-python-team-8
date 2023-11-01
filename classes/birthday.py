from datetime import datetime
from classes.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y'))
        except ValueError:
            raise ValueError("Invalid birthday format. Expected 'dd.mm.yyyy'.")

    def __str__(self):
        return datetime.strftime(self.value, '%d.%m.%Y')

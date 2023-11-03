from datetime import datetime
from classes.field import Field
from datetime import datetime, date


class Birthday(Field):
    def __init__(self, value):
        if isinstance(value, date):  # Make sure to use 'date' not 'datetime.date'
            super().__init__(value)
        else:
            try:
                parsed_date = datetime.strptime(value, '%d.%m.%Y')
                super().__init__(parsed_date)
            except ValueError:
                raise ValueError("Invalid birthday format. Expected 'dd.mm.yyyy'.")

    def __str__(self):
        return self.value.strftime('%d.%m.%Y')


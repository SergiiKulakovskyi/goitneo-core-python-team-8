import re
from classes.field import Field


class Email(Field):
    def __init__(self, value=None):
        if re.findall(r"[A-Za-z][A-Za-z0-9_.]+@[a-z]+\.[a-z]{2,}\b", value):
            self.value = value
        else:
            raise ValueError(f'Your email: {value} is incorrect!')

    def __str__(self):
        return self.value

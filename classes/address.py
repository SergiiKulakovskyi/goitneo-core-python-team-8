from classes.field import Field

class Address(Field):
    def __init__(self, address = None):
        self.address = address

    def __str__(self):
        return self.address
from classes.field import Field

class Address(Field):
    def __init__(self, address = None):
        super().__init__(address)

    def __str__(self):
        return self.value
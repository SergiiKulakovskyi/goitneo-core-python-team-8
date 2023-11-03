from classes.name import Name
from classes.phone import Phone
from classes.birthday import Birthday
from classes.address import Address
from classes.email import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = None         # Змінив зі списку на 1 параметр
        self.birthday = None
        self.address = None
        self.email = None
        

    # phone
    def add_phone(self, phone_number):      # Прибрав список
        self.phone = Phone(phone_number)

    def remove_phone(self):       # Прибрав список
        self.phone = None

    def edit_phone(self, old_phone_number, new_phone_number):   # Прибрав список
        self.phone = new_phone_number            
    
    
    # email
    def add_email(self, email):
        self.email = Email(email)
    
    def remove_email(self, email):
        self.email = None


    # address
    def add_address(self, address):
        self.address = Address(address)
    
    def remove_address(self):
        self.address = None


    # birthday
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {self.phone}, email: {self.email}, \
              birthday: {self.birthday}, address: {self.address}"

from classes.name import Name
from classes.phone import Phone
from classes.email import Email
from classes.address import Address
from classes.birthday import Birthday
from classes.address import Address
from classes.email import Email

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.email = None
        self.address = None
        self.birthday = None

        

    # phone
    def add_phone(self, phone_number):      # Прибрав список
        self.phone = Phone(phone_number)

    def remove_phone(self):       # Прибрав список
        self.phone = None

    def edit_phone(self, new_phone_number):   # Прибрав список
        self.phone = new_phone_number            
    
    
    # email
    def add_email(self, email):
        self.email = Email(email)
    
    def remove_email(self):
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
        phone_str = f', phone: {self.phone.value}' if self.phone else ''
        email_str = f', email: {self.email.value}' if self.email else ''
        address_str = f', address: {self.address.value}' if self.address else ''
        birthday_str = f', birthday: {self.birthday.value}' if self.birthday else ''
        return f"Contact name: {self.name.value}{phone_str}{email_str}{address_str}{birthday_str}"

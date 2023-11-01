from classes.record import Record
from decorators.input_error import input_error


@input_error
def add_contact(args, book):
    name = args.name 
    phone = args.phone
    
    if name not in book.data:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    else:
        return "Contact with the same name already exists."

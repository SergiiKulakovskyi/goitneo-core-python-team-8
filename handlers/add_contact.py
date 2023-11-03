from classes.record import Record
from decorators.input_error import input_error


@input_error()
def add_contact(args, book):
    name = args.name
    phone = args.phone
    email = args.email
    address = args.address
    birthday = args.birthday

    if name not in book.data:
        record = Record(name)
        if phone:
            record.add_phone(phone)
        if email:
            record.add_email(email)
        if address:
            record.add_address(address)
        if birthday:
            record.add_birthday(birthday)
        book.add_record(record)
        return "Contact added."
    else:
        return "Contact with the same name already exists."

from decorators.input_error import input_error


@input_error
def change_contact(args, book):
    name = args.name
    new_phone = args.phone
    email = args.email
    birthday = args.birthday
    address = args.address

    if name in book.data:
        record = book.find(name)
        record.edit_phone(new_phone)
        record.add_email(email)
        record.add_birthday(birthday)
        record.add_address(address)
        return "Contact updated."
    else:
        return "Contact not found."

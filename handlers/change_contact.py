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

        if new_phone is not None:
            record.edit_phone(new_phone)
        if email is not None:
            record.add_email(email)
        if birthday is not None:
            record.add_birthday(birthday)
        if address is not None:
            record.add_address(address)

        return "Contact updated."
    else:
        return "Contact not found."

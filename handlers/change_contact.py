from decorators.input_error import input_error


@input_error
def change_contact(args, book):
    name = args.name
    new_phone = args.phone

    if name in book.data:
        record = book.find(name)
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact updated."
    else:
        return "Contact not found."

from decorators.input_error import input_error
from utils.args_parser import count_non_empty_args


@input_error()
def change_contact(args, book):
    name = args.name
    new_phone = args.phone
    email = args.email
    birthday = args.birthday
    address = args.address

    if (count_non_empty_args(args) == 1):
        raise ValueError("Please specify the fields you want to change")

    if name in book.data:
        record = book.find(name)

        if new_phone is not None:
            record.add_phone(new_phone)
        if email is not None:
            record.add_email(email)
        if birthday is not None:
            record.add_birthday(birthday)
        if address is not None:
            record.add_address(address)

        return "Contact updated."
    else:
        raise ValueError("Contact not found.")

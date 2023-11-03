from classes.address_book import AddressBook
from decorators.input_error import input_error


@input_error()
def delete_contact(args, book: AddressBook):
    name = args.name
    fields = args.fields

    if fields is None:
        book.delete(name)
        return f'Contact "{name}" has been deleted'

    if name in book.data:
        record = book.find(name)
        if 'phone' in fields:
            record.remove_phone()
        if 'address' in fields:
            record.remove_address()
        if 'email' in fields:
            record.remove_email()
        if 'birthday' in fields:
            record.remove_birthday()

    return f"Field{'s' if len(fields) > 1 else ''} {', '.join(fields)} removed from contact {name}"

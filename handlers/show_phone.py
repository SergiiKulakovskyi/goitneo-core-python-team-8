from decorators.input_error import input_error


@input_error
def show_phone(args, book):
    name = args
    if name in book.data:
        record = book.find(name)
        return record.phones.value
    else:
        return "Contact not found."

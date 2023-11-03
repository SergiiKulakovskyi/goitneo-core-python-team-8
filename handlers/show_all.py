from decorators.input_error import input_error


@input_error
def show_all(book):
    contacts = []
    for record in book.data.values():
        contacts.append(str(record))
    return "\n".join(contacts)

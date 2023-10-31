from decorators.input_error import input_error


@input_error
def show_all(book):
    contacts = []
    for record in book.data.values():
        contacts.append(f"{record.name.value}: {record.phones[0].value}")
    return "\n".join(contacts)

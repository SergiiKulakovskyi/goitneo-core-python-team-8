from decorators.input_error import input_error


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday}."
    elif record and not record.birthday:
        return f"{name} has no birthday set."
    else:
        return f"Contact {name} not found."

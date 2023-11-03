from classes.record import Record


def add_email(args, book):
    name = args.name 
    email = args.email

    
    if name in book.data:
        record = book.find(name)
        record.add_email(email)
        book.add_record(record)
        return "Email updated."
    else:
        return "Contact not found."

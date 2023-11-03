from classes.record import Record


def remove_email(args, book):
    name = args.name 

    
    if name in book.data:
        record = book.find(name)
        record.remove_email()
        book.add_record(record)
        return "Email removed."
    else:
        return "Contact not found."

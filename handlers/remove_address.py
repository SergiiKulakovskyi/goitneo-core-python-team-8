from classes.record import Record


def remove_address(args, book):
    name = args.name 

    
    if name in book.data:
        record = book.find(name)
        record.remove_address()
        book.add_record(record)
        return "Address removed."
    else:
        return "Contact not found."

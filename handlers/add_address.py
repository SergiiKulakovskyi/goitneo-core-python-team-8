from classes.record import Record


def add_address(args, book):
    name = args.name 
    email = args.address

    
    if name in book.data:
        record = book.find(name)
        record.add_address(email)
        book.add_record(record)
        return "Address updated."
    else:
        return "Contact not found."

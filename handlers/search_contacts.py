from classes.address_book import AddressBook
from utils.representation import display_contacts

def search_contacts(args, book: AddressBook):
    criteria = args.criteria
    search_text = args.text.lower()

    records = book.values()
    filtered_values = [record for record in records if search_text in str(getattr(
        record, criteria, '')).lower()]

    return display_contacts(filtered_values)

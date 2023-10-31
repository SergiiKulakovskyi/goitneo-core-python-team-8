import os
from classes.address_book import AddressBook
import pickle

subfolder_path = 'data'

if not os.path.exists(subfolder_path):
    os.makedirs(subfolder_path)


def save_to_file(book, filename='address_book.pkl'):
    file_path = os.path.join(subfolder_path, filename)
    with open(file_path, 'wb') as file:
        pickle.dump(book, file)


def load_from_file(filename='address_book.pkl'):
    file_path = os.path.join(subfolder_path, filename)
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return AddressBook()

import os
import pickle

subfolder_path = 'data'

if not os.path.exists(subfolder_path):
    os.makedirs(subfolder_path)


def save_to_file(obj, filename):
    file_path = os.path.join(subfolder_path, filename)
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)


def load_from_file(filename, default_class):
    file_path = os.path.join(subfolder_path, filename)
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return default_class()

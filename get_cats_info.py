from pathlib import Path
from typing import List


def get_cats_info(file_path: str) -> List[dict]:
    """Function to get the information of all cats from a file.

        __args__:
            file_path: str
                The path to the file containing the cats' information.
                Each line in the file contains the id, name and age of a cat.
                Separated by a comma.
        __return__:
            dict
                A dictionary containing the information of all cats.
                The keys are 'id', 'name' and 'age' and the values are the corresponding values."""
    file_path = Path(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Open the file and read the lines
            lines = file.readlines()
        # Process the lines to list of dictionaries of name, age, and color
        cats = []
        for line in lines:
            cats.append(dict(zip(['id', 'name', 'age'], line.strip().split(','))))
        return cats
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except IsADirectoryError:
        print(f"{file_path} is a directory.")
        return []
    except IOError:
        print(f"Could not read file {file_path}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

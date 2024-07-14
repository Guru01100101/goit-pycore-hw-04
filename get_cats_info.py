from pathlib import Path
from pprint import pprint
from typing import List


def get_cats_info(file_path: str) -> List[dict]:
    """
    Function to get the information of all cats from a file.

        __args__:
            file_path: str
                The path to the file containing the cats' information.
                Each line in the file contains the id, name and age of a cat.
                Separated by a comma.
        __return__:
            dict
                A dictionary containing the information of all cats.
                The keys are 'id', 'name' and 'age' and the values are the corresponding values.
                """
    file_path = Path(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Open the file and read the lines
            lines = file.readlines()
        # Process the lines to list of dictionaries of name, age, and color
        cats = []
        for line in lines:
            cats.append({
                "id": line.strip().split(',')[0],
                "name": line.strip().split(',')[1],
                "age": int(line.strip().split(',')[2])
            })
        return cats
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except IsADirectoryError:
        print(f"{file_path} is a data.")
        return []
    except IOError:
        print(f"Could not read file {file_path}.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def main():
    cats_info = get_cats_info("data/cats.txt")
    pprint(cats_info, indent=4, sort_dicts=False)
    """
    Expected output: 
    [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
    ]
    """


if __name__ == '__main__':
    main()

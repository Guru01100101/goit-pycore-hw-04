import argparse
import json

from normalize_phone import normalize_phone


def load_phonebook() -> dict:
    try:
        with open("phonebook.json", "r") as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = {}
    return phonebook


def save_phonebook(phonebook: dict) -> None:
    with open("phonebook.json", "w") as file:
        json.dump(phonebook, file, indent=4)


def add_contact(name: str, phone: str) -> None:
    ...


def change_contact(name: str, new_phone: str) -> None:
    ...


def delete_contact(name: str) -> None:
    ...


def search_contact(pattern: str) -> None:
    ...


def show_phonebook():
    ...


def main(phonebook=None):
    print("Welcome to the assistant bot!")
    while True:
        command = input("command: ").strip().lower().split()

        if command[0] in ["close", "exit"]:
            print("Good bye!")
            break
        elif command[0] == "hello":
            print("How can I help you?")
        elif command[0] == "add":
            if len(command) != 3:
                print("Invalid command.")
                print("Usage: add <name> <phone>")
                continue
            add_contact(command[1], command[2])
        elif command[0] == "change":
            if len(command) != 3:
                print("Invalid command.")
                print("Usage: change <name> <phone>")
                continue
            change_contact(command[1], command[2])
        elif command[0] == "delete":
            if len(command) != 2:
                print("Invalid command.")
                print("Usage: delete <name>")
                continue
            delete_contact(command[1])
        elif command[0] == "search":
            if len(command) != 2:
                print("Invalid command.")
                print("Usage: search <pattern>")
                continue
            search_contact(command[1])
        elif command[0] == "show":
            if len(command) == 1 or (len(command) == 2 and command[1] == "all"):
                show_phonebook()
            elif len(command) == 2:
                search_contact(command[1])
            else:
                print("Invalid command.")
                print("Usage: show [pattern]")
        else:
            print("Invalid command.")
            print("Available commands: hello, add, change, delete, search, show, close, exit")


if __name__ == '__main__':
    phonebook = load_phonebook()
    main(phonebook=phonebook)
    save_phonebook(phonebook)

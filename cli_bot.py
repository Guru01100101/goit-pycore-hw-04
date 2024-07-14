import argparse
import json

from normalize_phone import normalize_phone


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


def main():
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

# TODO: Decide if you want to use the command_line_handler function or the main function. You can't use both.
# def command_line_handler():
#     parser = argparse.ArgumentParser(description="Phonebook CLI")
#     parser.add_argument("command",
#                         type=str,
#                         help="The command to execute.")
#     parser.add_argument("name",
#                         type=str,
#                         nargs="?",
#                         help="The name of the contact.")
#     parser.add_argument("phone",
#                         type=str,
#                         nargs="?",
#                         help="The phone number of the contact.")
#     args = parser.parse_args()
#     command = args.command
#     name = args.name
#     phone = args.phone
#
#     if command == "add":
#         add_contact(name, phone)
#     elif command == "change":
#         change_contact(name, phone)
#     elif command == "delete":
#         delete_contact(name)
#     elif command == "search":
#         search_contact(name=name, phone=phone)
#     elif command == "show":
#         show_phonebook()
#     else:
#         print("Invalid command.")
#         sys.exit(1)

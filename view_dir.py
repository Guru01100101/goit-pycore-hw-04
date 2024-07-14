import argparse
import os

from pathlib import Path
from colorama import Fore, Style


def print_dir_tree(root_dir: str, prefix='') -> None:
    """Function to print the directory tree.

        __args__:
            root_dir: str
                The path to the root directory.
            prefix: str
                The prefix to be added to the directory tree.
        __return__:
            None"""
    root_dir = Path(root_dir)  # Convert the root_dir to a Path object
    try:
        # Check if the root_dir is a directory and print it in blue
        if root_dir.is_dir():
            print(f"{prefix}{Fore.BLUE}{root_dir.name}{Style.RESET_ALL}/")
            for item in root_dir.iterdir():
                # Check if the item is a directory or a file and print accordingly in different colors
                if item.is_dir():
                    print_dir_tree(item, prefix + '  ')
                else:
                    print(f"{prefix}  {Fore.GREEN}{item.name}{Style.RESET_ALL}")
        else:
            print(f"{prefix}{Fore.GREEN}{root_dir.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Print the directory tree.")
    parser.add_argument("root_dir",
                        type=str,
                        nargs="?",
                        default=Path.cwd(),
                        help="The path to the root directory.")
    parser.add_argument("--prefix",
                        type=str,
                        nargs="?",
                        default='',
                        help="The prefix to be added to the directory tree.")
    args = parser.parse_args()
    root_dir = args.root_dir
    prefix = args.prefix

    if not os.path.exists(root_dir):
        print(f"Directory {root_dir} does not exist.")
        return None

    print_dir_tree(root_dir, prefix=prefix)


if __name__ == '__main__':
    main()

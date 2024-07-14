from pathlib import Path


def total_salary(file_path: str) -> tuple:
    """Function to calculate the total salary and average salary of all employees.

        __args__:
            file_path: str
                The path to the file containing the salaries.
                Each line in the file contains the name and the salary of an employee.
                Separated by a comma.
        __return__:
            tuple(int, int)
                The total salary of all employees.
             The average salary of all employees."""
    file_path = Path(file_path)

    try:
        with open(file_path, 'r') as file:
            # Open the file and read the lines
            lines = file.readlines()
        # Process the lines to list of dictionaries of name and salary
        employees = []
        for line in lines:
            employees.append(dict(zip(['name', 'salary'], line.strip().split(','))))

        # Calculate the total salary
        total = sum([float(employee['salary']) for employee in employees])

        # Calculate the average salary
        average_salary = total / len(employees)
        return total, average_salary
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None, None
    except IsADirectoryError:
        print(f"{file_path} is a directory.")
        return None, None
    except IOError:
        print(f"Could not read file {file_path}.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
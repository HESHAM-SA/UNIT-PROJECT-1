# person.py
import json

class Person:
    def __init__(self, name: str, id_number: str, city: str, password: str):
        self.name = name
        self.city = city
        # Setters are called to validate data upon object creation
        self.set_id_number(id_number)
        self.set_password(password)

    def set_password(self, password):
        """Validates and sets the user's password."""
        if len(password) < 3:
            raise ValueError('Password must be at least 3 characters long.')
        self.password = password
        print(f'Password for {self.name} set successfully.')
        return self.password

    def set_id_number(self, id_number):
        """Validates the ID number format and ensures it is unique across all users."""
        if not id_number.isdigit() or len(id_number) != 3:
            raise ValueError('ID number must be exactly 3 digits.')

        teachers_file_path = 'data/teachers.json'
        students_file_path = 'data/students.json' # <-- BUG FIX: Was pointing to teachers.json

        # Check for ID uniqueness in teachers file
        try:
            with open(teachers_file_path, 'r', encoding='UTF-8') as file:
                teachers = json.load(file)
            for teacher in teachers:
                if id_number == teacher['id_number']:
                    raise ValueError('This ID number is already taken. Please choose another one.')
        except FileNotFoundError:
            # This is normal if it's the first teacher registering
            pass
        except json.JSONDecodeError:
            # This is normal if the file is empty
            pass

        # Check for ID uniqueness in students file
        try:
            with open(students_file_path, 'r', encoding='UTF-8') as file:
                students = json.load(file)
            for student in students:
                if id_number == student['id_number']:
                    raise ValueError('This ID number is already taken. Please choose another one.')
        except FileNotFoundError:
            # This is normal if it's the first student registering
            pass
        except json.JSONDecodeError:
             # This is normal if the file is empty
            pass

        self.id_number = id_number
        print(f'ID number {self.id_number} set successfully.')
        return self.id_number

    def introduce_yourself(self):
        """Prints a simple introduction for the person."""
        print(f"Hello, I am {self.name}, and I come from {self.city}.")
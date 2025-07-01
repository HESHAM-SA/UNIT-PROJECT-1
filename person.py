# person.py
from utils import load_json_file, hash_password


class Person:
    def __init__(self, name: str, id_number: str, city: str, password: str) -> None:
        self.name = name
        self.city = city
        self.set_id_number(id_number)
        self.set_password(password)

    def set_password(self, password: str) -> str:
        """Validates and sets the user's password (hashed)."""
        if len(password) < 3:
            raise ValueError('Password must be at least 3 characters long.')
        self.password = hash_password(password)
        print(f'Password for {self.name} set successfully.')
        return self.password

    def set_id_number(self, id_number: str) -> str:
        """Validates the ID number format and ensures it is unique across all users."""
        if not id_number.isdigit() or len(id_number) != 3:
            raise ValueError('ID number must be exactly 3 digits.')

        teachers_file_path = 'data/teachers.json'
        students_file_path = 'data/students.json'

        # Check for ID uniqueness in teachers file
        teachers = load_json_file(teachers_file_path)
        for teacher in teachers:
            if id_number == teacher['id_number']:
                raise ValueError('This ID number is already taken. Please choose another one.')

        # Check for ID uniqueness in students file
        students = load_json_file(students_file_path)
        for student in students:
            if id_number == student['id_number']:
                raise ValueError('This ID number is already taken. Please choose another one.')

        self.id_number = id_number
        print(f'ID number {self.id_number} set successfully.')
        return self.id_number

    def introduce_yourself(self) -> None:
        """Prints a simple introduction for the person."""
        print(f"Hello, I am {self.name}, and I come from {self.city}.")
from utils import load_json_file, hash_password, console


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
        return self.password

    def set_id_number(self, id_number: str) -> str:
        """Validates the ID number format and ensures it is unique across all users."""
        if not id_number.isdigit() or len(id_number) != 3:
            raise ValueError('ID number must be exactly 3 digits.')

        teachers = load_json_file('data/teachers.json')
        students = load_json_file('data/students.json')
        
        all_ids = [p['id_number'] for p in teachers] + [s['id_number'] for s in students]
        
        if id_number in all_ids:
            raise ValueError('This ID number is already taken. Please choose another one.')

        self.id_number = id_number
        return self.id_number

    def introduce_yourself(self) -> None:
        """Prints a simple introduction for the person."""
        console.print(f"Hello, I am {self.name}, and I come from {self.city}.")

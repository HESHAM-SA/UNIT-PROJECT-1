import person 
import json
import os

class Student(person.Person):
    def __init__(self, name, id_number, city, password, level):
        super().__init__(name, id_number, city, password)
        self.set_level(level)

    def set_level(self, level):
        levels = ['1', '2', '3']
        if level not in levels:
            raise Exception (f'please enter one of those levels: {levels}')

        else:
            self.level = level
            return self.level
        
    @staticmethod
    def register_new_user(): 
        file_path = 'data/students.json'    
        os.makedirs(os.path.dirname(file_path), exist_ok=True) 
        all_students = []
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                all_students = json.load(file)
        except Exception as e:
            all_students = []
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_students, file, indent=2)
        try:                           
            name = input('Enter your name: ')
            id_number = input('Enter your id number: ')
            city = input('Enter your city: ')
            password = input('Enter your passowerd')
            level = input ('Enter your level: ')
            student = Student(name, id_number, city, password, level)
            all_students.append(student.__dict__)
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_students, file, indent=2)
        except Exception as e:
            print(e)




    @staticmethod
    def log_in(id_number, password):
        file_path = 'data/students.json'
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                students = json.load(file)

            for student in students:
                if id_number == student.get('id_number') and password == student.get('password'):
                    print(f"Wellcome {student['name']}")
                    return True
        except Exception as e:
            print(e)
        return False

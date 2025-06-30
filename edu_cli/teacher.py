import person
import json
import os 


class Teacher(person.Person):
    def __init__(self, name, id_number, city, password, major):
        super().__init__(name, id_number, city, password)
        self.set_major(major)
        

    # abstraction one of prensibls of oop
    def set_major(self, major):
        majors = ['math','history','computer']
        if major not in majors:
            raise Exception('please chose from those:', majors)
        else:
            self.major = major
            return self.major


    @staticmethod
    def register_new_user():
        file_path = 'data/teachers.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        all_teachers = []

        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                all_teachers = json.load(file)
        except Exception as e:
            all_teachers = []
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_teachers, file, indent=2)

        try:
            name = input('Enter your name: ')
            id_number = input('Enter id number from 3 digits: ')
            city = input('Enter your city: ')
            password  = input('Enter your password: ')
            major = input('Enter your major: ')
            teacher = Teacher(name, id_number, city, password, major)
            all_teachers.append(teacher.__dict__)
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_teachers, file, indent=2)  
                print(f'Registration successful! Welcome Teacher: {teacher.name}')
        except Exception as e:
            print(e)

    @staticmethod
    def log_in(id_number, password):
        with open('data/teachers.json', 'r', encoding='UTF-8') as file:
            teachers = json.load(file)

        for teacher in teachers:
            if id_number == teacher.get('id_number') and password == teacher.get('password'):
                print(f"Wellcome {teacher['name']}")
                return True
        print('ID or password is invalid')
        return False
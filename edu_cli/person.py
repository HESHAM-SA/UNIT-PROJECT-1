import json


class Person:
    def __init__(self, name:str, id_number:str, city:str, password:str):
        self.name = name
        self.city = city
        self.set_id_number(id_number)
        self.set_password(password)
        

    def set_password(self, password):
         if len(password) < 3:
              raise Exception ('please entre password more then 3 letters')
         else:
              self.password = password
              print(f'your password is {self.password}')
              return self.password

    
    def set_id_number(self, id_number):
        if len(id_number) != 3: 
            raise Exception('please enter 3 numbers')
        teachers_file_path = 'data/teachers.json'
        students_file_path = 'data/teachers.json'
        try:
            with open(teachers_file_path, 'r', encoding='UTF-8') as file:
                teachers = json.load(file)
            for teacher in teachers:
                if id_number == teacher['id_number']:
                        raise Exception('This id number is taken please chose other one')
        except FileNotFoundError:
             print('person method teacher')
        
        try:
            with open(students_file_path, 'r', encoding='UTF-8') as file:
                students = json.load(file)
            for student in students:
                    if id_number == student['id_number']:
                        raise Exception('This id number is taken please chose other one')
        except FileNotFoundError:
            print('person method student')


        self.id_number = id_number
        print(f'ID number {self.id_number} set successfully.')
        return self.id_number



    def interduse_your_self(self):
        print(f"I am {self.name}, and i come from {self.city}")
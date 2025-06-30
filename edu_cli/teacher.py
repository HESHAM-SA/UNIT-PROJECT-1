import person
import json
import os 
import random

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
    

    def create_quize(number_qustions:int):
        file_path = 'data/qustions.json'
        qustions = []
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                qustions = json.load(file)
        except FileNotFoundError as e:
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(qustions)
                print(e + 'but now we create empty list []')

        random.shuffle(qustions)
        for i in range(number_qustions):
            print(qustions[i].keys(), end='')
            q = qustions[i].values()
            print(list(q)[0].keys())



    def add_qustion():
        qustions = []
        file_path = 'data/qustions.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                qustions = json.load(file)
        except FileNotFoundError as e:
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(qustions, file)
            print(e)

        while True:
            add_more_qustion = input('Do you want to add more qustion? (y/n): ')
            if add_more_qustion == 'y':
                    q = input('Enter your True False qustion: ')
                    user_answer = '''
                    1. True
                    2. False
                    '''
                    answer = int(input(user_answer))
                    match answer:
                        case 1:
                            value = {q:True}
                        case 2:
                            value = {q:False}
                    key = f'Q_{len(qustions) + 1}'
                    qustion = {key:value}
                    qustions.append(qustion)
            else:
                break
        
        try:
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(qustions, file, indent=2)
        except Exception as e:
            print(e)


# Teacher.add_qustion()
Teacher.create_quize(2)



            




import person 
import json
import os
import pandas as pd
import random
import numpy as np


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
            password = input('Enter your passowerd: ')
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



    def display_students():

        try:
            with open('data/students.json', 'r', encoding='UTF-8') as file:
                students = json.load(file)
                students = [student['name'] for student in students]
                s = pd.Series(students)
                print(s)
        except FileNotFoundError:
            print('No students in file')


    def devide_students_groubs(group_number:int):
        try:
            with open('data/students.json', 'r', encoding='UTF-8') as file:
                students = json.load(file)
                students = [student['name'] for student in students]
 
                groups = []
                random.shuffle(students)
                for i in range(len(students)):
                    if i % group_number == 0:
                        groups.append(students[i: i+ group_number])
        except FileNotFoundError:
            print('No file with students.json name')
        else:
            for i, group in enumerate(groups):
                print(f"Group {i}: {group}")

Student.devide_students_groubs(2)
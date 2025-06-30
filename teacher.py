# teacher.py
import person
import json
import os
import random

class Teacher(person.Person):
    def __init__(self, name, id_number, city, password, major):
        super().__init__(name, id_number, city, password)
        self.set_major(major)

    def set_major(self, major):
        """Validates and sets the teacher's major."""
        # This is a good example of encapsulation, ensuring data integrity.
        valid_majors = ['math', 'history', 'computer science']
        if major.lower() not in valid_majors:
            raise ValueError(f'Invalid major. Please choose from: {", ".join(valid_majors)}')
        self.major = major
        return self.major

    @staticmethod
    def register():
        """Handles the registration process for a new teacher."""
        file_path = 'data/teachers.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        all_teachers = []
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                all_teachers = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_teachers = []

        try:
            name = input('Enter your name: ')
            id_number = input('Enter your 3-digit ID number: ')
            city = input('Enter your city: ')
            password = input('Enter your password: ')
            major = input('Enter your major (e.g., math, history, computer science): ')
            new_teacher = Teacher(name, id_number, city, password, major)
            all_teachers.append(new_teacher.__dict__)
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_teachers, file, indent=4)
            print(f'Registration successful! Welcome, Teacher {name}.')
        except (ValueError, Exception) as e:
            print(f"Registration failed: {e}")

    @staticmethod
    def log_in(id_number, password):
        """Logs in a teacher by verifying their ID and password."""
        file_path = 'data/teachers.json'
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                teachers = json.load(file)
            for teacher in teachers:
                if id_number == teacher.get('id_number') and password == teacher.get('password'):
                    print(f"Welcome, {teacher['name']}!")
                    return True
            print('Invalid ID number or password.')
            return False
        except (FileNotFoundError, json.JSONDecodeError):
            print("No teacher data found. Please register first.")
            return False

    @staticmethod
    def create_quiz(number_of_questions: int):
        """Creates a new quiz from the question bank."""
        bank_path = 'data/questions.json'
        question_bank = []
        try:
            with open(bank_path, 'r', encoding='UTF-8') as file:
                question_bank = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Question bank is empty or not found. Please add questions first.")
            return

        if len(question_bank) < number_of_questions:
            print(f"Error: You requested {number_of_questions} questions, but only {len(question_bank)} are available in the bank.")
            return

        selection_prompt = "How would you like to select questions?\n1. Randomly select questions\n2. Use the last questions added\n"
        selection_choice = input(selection_prompt)
        quiz_questions = []

        if selection_choice == '1':
            quiz_questions = random.sample(question_bank, number_of_questions)
            print("Selected random questions.")
        elif selection_choice == '2':
            # BUG FIX: .tail() is for pandas, not lists. Use slicing instead.
            quiz_questions = question_bank[-number_of_questions:]
            print("Selected the last questions from the bank.")
        else:
            print("Invalid selection.")
            return

        print("\n--- Generated Quiz Preview ---")
        for i, q in enumerate(quiz_questions, 1):
            question_text = list(q.keys())[0]
            answer = "True" if list(q.values())[0] else "False"
            print(f"{i}. {question_text} (Answer: {answer})")

        save_choice = input('\nDo you want to save this as the active quiz for students? (y/n): ').lower()
        if save_choice == 'y':
            quiz_path = 'data/quiz.json'
            with open(quiz_path, 'w', encoding='UTF-8') as file:
                json.dump(quiz_questions, file, indent=4)
            print("Quiz saved and is now active for students.")
        else:
            print("Quiz creation cancelled.")

    @staticmethod
    def add_question_to_bank():
        """Adds new True/False questions to the question bank."""
        file_path = 'data/questions.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        question_bank = []
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                question_bank = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            question_bank = []

        while True:
            add_more = input('Do you want to add a new question? (y/n): ').lower()
            if add_more == 'y':
                question_text = input('Enter the new True/False question statement: ')
                answer_prompt = "Is the correct answer True or False?\n1. True\n2. False\n"
                answer_choice = input(answer_prompt)
                
                if answer_choice == '1':
                    correct_answer = True
                elif answer_choice == '2':
                    correct_answer = False
                else:
                    print("Invalid choice. Question not added.")
                    continue
                
                new_question = {question_text: correct_answer}
                question_bank.append(new_question)
                print("Question added to the bank.")
            else:
                break

        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump(question_bank, file, indent=4)
        print("Question bank has been updated.")
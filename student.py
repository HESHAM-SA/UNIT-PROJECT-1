# student.py
import person
import json
import os
import pandas as pd
import random

class Student(person.Person):
    def __init__(self, name, id_number, city, password, exams=None):
        super().__init__(name, id_number, city, password)
        # Each student starts with no exam history
        self.exams = exams if exams is not None else []

    @staticmethod
    def register():
        """Handles the registration process for a new student."""
        file_path = 'data/students.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        all_students = []
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                all_students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            all_students = []

        try:
            name = input('Enter your name: ')
            id_number = input('Enter your 3-digit ID number: ')
            city = input('Enter your city: ')
            password = input('Enter your password: ')
            new_student = Student(name, id_number, city, password)
            all_students.append(new_student.__dict__)
            with open(file_path, 'w', encoding='UTF-8') as file:
                json.dump(all_students, file, indent=4)
            print(f"Registration successful! Welcome, {name}.")
        except (ValueError, Exception) as e:
            print(f"Registration failed: {e}")

    @staticmethod
    def log_in(id_number, password):
        """Logs in a student by verifying their ID and password."""
        file_path = 'data/students.json'
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                students = json.load(file)
            for student in students:
                if id_number == student.get('id_number') and password == student.get('password'):
                    print(f"Welcome, {student['name']}!")
                    return True
            print("Invalid ID number or password.")
            return False
        except (FileNotFoundError, json.JSONDecodeError):
            print("No student data found. Please register first.")
            return False

    @staticmethod
    def display_all_students():
        """Displays a list of all registered students' names."""
        try:
            with open('data/students.json', 'r', encoding='UTF-8') as file:
                students = json.load(file)
                student_names = [student['name'] for student in students]
                student_series = pd.Series(student_names, name="Registered Students")
                print(student_series)
        except (FileNotFoundError, json.JSONDecodeError):
            print('No student data found.')

    @staticmethod
    def divide_students_into_groups(group_size: int):
        """Randomly divides students into groups of a specified size."""
        try:
            with open('data/students.json', 'r', encoding='UTF-8') as file:
                students = json.load(file)
                student_names = [student['name'] for student in students]

                if not student_names:
                    print("There are no students to divide.")
                    return

                random.shuffle(student_names)
                groups = [student_names[i:i + group_size] for i in range(0, len(student_names), group_size)]

                print("\n--- Student Groups ---")
                for i, group in enumerate(groups, 1):
                    print(f"Group {i}: {', '.join(group)}")
                print("----------------------")

        except FileNotFoundError:
            print('Could not find the students.json file.')
        except ValueError:
            print("Invalid group size. Please enter a positive number.")

    @staticmethod
    def show_score(id_number: str):
        """Displays the most recent exam score for a given student."""
        with open('data/students.json', 'r', encoding='UTF-8') as file:
            all_students = json.load(file)

        # Find the specific student's data
        student_data = next((s for s in all_students if s['id_number'] == id_number), None)

        if not student_data:
            print("Student not found.")
            return

        if not student_data['exams']:
            print("You have not taken any quizzes yet.")
        else:
            # Show the score of the most recent exam
            last_exam = student_data['exams'][-1]
            print(f"Your score on the last quiz was: {last_exam['score']}")

    @staticmethod
    def take_quiz(id_number: str):
        """Allows a student to take the currently active quiz."""
        try:
            with open('data/quiz.json', 'r', encoding='UTF-8') as file:
                quiz_questions = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("There is no quiz available at the moment. Please ask your teacher to create one.")
            return

        user_ready = input(f'The quiz has {len(quiz_questions)} questions. Are you ready to begin? (y/n): ').lower()
        if user_ready != 'y':
            print("Quiz cancelled.")
            return

        student_answers = []
        student_score = 0
        answer_menu = "Choose your answer (1=True, 2=False): "

        print("\n--- Starting Quiz ---")
        for i, question_data in enumerate(quiz_questions, 1):
            question_text = list(question_data.keys())[0]
            correct_answer_is_true = list(question_data.values())[0]

            print(f"\nQ{i}: {question_text}")
            try:
                user_choice = int(input(answer_menu))
                user_answer_is_true = (user_choice == 1)

                student_answers.append(user_answer_is_true)
                if user_answer_is_true == correct_answer_is_true:
                    student_score += 1
                    print("Correct!")
                else:
                    print("Incorrect.")
            except ValueError:
                print("Invalid input. Marking as incorrect.")
                student_answers.append(None) # Mark as unanswered

        print(f'\n--- Quiz Finished ---\nYour final score is: {student_score}/{len(quiz_questions)}')

        # Load student data to save the score
        with open('data/students.json', 'r', encoding='UTF-8') as file:
            all_students = json.load(file)

        # Find the student and update their record
        student_found = False
        for student in all_students:
            if student['id_number'] == id_number:
                student['exams'].append({'score': student_score})
                student_found = True
                break

        # Save the updated student data
        if student_found:
            with open('data/students.json', 'w', encoding='UTF-8') as file:
                json.dump(all_students, file, indent=4)
            print("Your score has been saved.")
        else:
            print("Error: Could not find your student record to save the score.")
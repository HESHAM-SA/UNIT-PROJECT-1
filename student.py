# student.py
import person
import pandas as pd
import random
from utils import load_json_file, save_json_file, get_valid_string, get_valid_int, verify_password


class Student(person.Person):
    def __init__(self, name: str, id_number: str, city: str, password: str, exams: list | None = None) -> None:
        super().__init__(name, id_number, city, password)
        # Each student starts with no exam history
        self.exams = exams if exams is not None else []

    @staticmethod
    def register() -> None:
        """Handles the registration process for a new student."""
        file_path = 'data/students.json'
        all_students = load_json_file(file_path)

        try:
            name = get_valid_string('Enter your name: ')
            id_number = get_valid_string('Enter your 3-digit ID number: ')
            city = get_valid_string('Enter your city: ')
            password = get_valid_string('Enter your password: ', 3)
            new_student = Student(name, id_number, city, password)
            all_students.append(new_student.__dict__)
            save_json_file(file_path, all_students)
            print(f"Registration successful! Welcome, {name}.")
        except (ValueError, Exception) as e:
            print(f"Registration failed: {e}")

    @staticmethod
    def log_in(id_number: str, password: str) -> bool:
        """Logs in a student by verifying their ID and password."""
        file_path = 'data/students.json'
        students = load_json_file(file_path)

        if not students:
            print("No student data found. Please register first.")
            return False

        for student in students:
            if id_number == student.get('id_number') and verify_password(student.get('password'), password):
                print(f"Welcome, {student['name']}!")
                return True
        print("Invalid ID number or password.")
        return False

    @staticmethod
    def display_all_students() -> None:
        """Displays a list of all registered students' names."""
        students = load_json_file('data/students.json')
        if not students:
            print('No student data found.')
            return

        student_names = [student['name'] for student in students]
        student_series = pd.Series(student_names, name="Registered Students")
        print(student_series)

    @staticmethod
    def divide_students_into_groups(group_size: int) -> None:
        """Randomly divides students into groups of a specified size."""
        students = load_json_file('data/students.json')
        if not students:
            print('Could not find the students.json file.')
            return

        student_names = [student['name'] for student in students]

        if not student_names:
            print("There are no students to divide.")
            return

        random.shuffle(student_names)
        groups = []
        for i in range(len(student_names)):
            if i % group_size == 0:
                group = student_names[i: i+group_size]
                groups.append(group)

        print("\n--- Student Groups ---")
        for i, group in enumerate(groups, 1):
            print(f"Group {i}: {', '.join(group)}")
        print("----------------------")

    # @staticmethod
    # def _search_for_student(id_number: str) -> dict | None:
    #     """To find specifc student with his id number"""
    #     file_path = 'data/students.json'
    #     all_students = load_json_file(file_path)
    #     student = None
    #     for s in all_students:
    #         if s['id_number'] == id_number:
    #             student = s
    #             break
    #     return student

    @staticmethod
    def show_score(id_number: str) -> None:
        """Displays the most recent exam score for a given student."""
        file_path = 'data/students.json'
        all_students = load_json_file(file_path)
        student = None
        for s in all_students:
            if s['id_number'] == id_number:
                student = s

        if not student:
            print("Student not found.")
            return

        if not student['exams']:
            print("You have not taken any quizzes yet.")
        else:
            # Show the score of the most recent exam
            last_exam = student['exams'][-1]
            print(f"Your score on the last quiz was: {last_exam['score']}")

    @staticmethod
    def take_quiz(id_number: str) -> None:
        """Allows a student to take the currently active quiz, preventing retakes."""
        quiz_questions = load_json_file('data/quiz.json')
        all_students = load_json_file('data/students.json')

        if not quiz_questions:
            print("No quiz is currently available. Please contact your teacher.")
            return

        if not all_students:
            print("Error: Could not find student records.")
            return

        student = None
        for s in all_students:
            if s['id_number'] == id_number:
                student = s

        if not student:
            print("Error: Could not find your student record.")
            return

        if student['exams']:
            print("\nOur records show you have already completed a quiz. You cannot retake it.")
            return

        print(f'The quiz has {len(quiz_questions)} questions.')
        while True:
            user_ready = input('Are you ready to begin? (y/n): ').lower().strip()
            if user_ready in ['y', 'yes']:
                break
            elif user_ready in ['n', 'no']:
                print("Quiz cancelled.")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

        student_score = 0
        final_question_results = []

        print("\n--- Starting Quiz ---")
        for i, question_data in enumerate(quiz_questions, 1):
            question_text = list(question_data.keys())[0]
            correct_answer = list(question_data.values())[0]

            print(f"\nQ{i}: {question_text}")
            user_answer = None
            while True:
                user_choice = get_valid_int("Choose your answer (1=True, 2=False): ")
                match user_choice:
                    case 1:
                        user_answer = True
                        if correct_answer == user_answer:
                            student_score += 1
                        break

                    case 2:
                        user_answer = False
                        if correct_answer == user_answer:
                            student_score += 1
                        break
                    case _:
                        print('invalid input')

            question_with_correction = {question_text: True if correct_answer == user_answer else False}
            final_question_results.append(question_with_correction)

        print(f'\n--- Quiz Finished ---\nYour final score is: {student_score}/{len(quiz_questions)}')
        # show for student list of qusitons and result (True or False)
        for i, q in enumerate(final_question_results, 1):
            print(f"\nQ{i}: {list(q.keys())[0]} {list(q.values())[0]}")

        student['exams'].append({'score': student_score})
        save_json_file('data/students.json', all_students)
        print("Your score has been saved.")
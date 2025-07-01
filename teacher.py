# teacher.py
import person
import random
from utils import load_json_file, save_json_file, get_valid_string, get_valid_int, verify_password


class Teacher(person.Person):
    def __init__(self, name: str, id_number: str, city: str, password: str, major: str) -> None:
        super().__init__(name, id_number, city, password)
        self.set_major(major)

    def set_major(self, major: str) -> str:
        """Validates and sets the teacher's major."""
        # This is a good example of encapsulation, ensuring data integrity.
        valid_majors = ['math', 'history', 'computer']
        if major.lower() not in valid_majors:
            raise ValueError(f'Invalid major. Please choose from: {", ".join(valid_majors)}')
        self.major = major
        return self.major

    @staticmethod
    def register() -> None:
        """Handles the registration process for a new teacher."""
        file_path = 'data/teachers.json'
        all_teachers = load_json_file(file_path)

        try:
            name = get_valid_string('Enter your name: ')
            id_number = get_valid_string('Enter your 3-digit ID number: ')
            city = get_valid_string('Enter your city: ')
            password = get_valid_string('Enter your password: ', 3)
            major = get_valid_string('Enter your major (e.g., math, history, computer): ')
            new_teacher = Teacher(name, id_number, city, password, major)
            all_teachers.append(new_teacher.__dict__)
            save_json_file(file_path, all_teachers)
            print(f'Registration successful! Welcome, Teacher {name}.')
        except (ValueError, Exception) as e:
            print(f"Registration failed: {e}")

    @staticmethod
    def log_in(id_number: str, password: str) -> bool:
        """Logs in a teacher by verifying their ID and password."""
        file_path = 'data/teachers.json'
        teachers = load_json_file(file_path)

        if not teachers:
            print("No teacher data found. Please register first.")
            return False

        for teacher in teachers:
            if id_number == teacher.get('id_number') and verify_password(teacher.get('password'), password):
                print(f"Welcome, teacher: {teacher['name']}!")
                return True
        print('Invalid ID number or password.')
        return False

    @staticmethod
    def create_quiz(number_of_questions: int) -> None:
        """Creates a new quiz from the question bank."""
        bank_path = 'data/questions.json'
        question_bank = load_json_file(bank_path)

        if not question_bank:
            print("Question bank is empty or not found. Please add questions first.")
            return

        if len(question_bank) < number_of_questions:
            print(f"Error: You requested {number_of_questions} questions, but only {len(question_bank)} are available in the bank.")
            return

        print("How would you like to select questions?")
        print("1. Randomly select questions")
        print("2. Use the last questions added")

        selection_choice = get_valid_int("Enter your choice: ")
        quiz_questions = []

        if selection_choice == 1:
            quiz_questions = random.sample(question_bank, number_of_questions)
            print("Selected random questions.")
        elif selection_choice == 2:
            quiz_questions = question_bank[-number_of_questions:]
            print("Selected the last questions from the bank.")

        print("\n--- Generated Quiz Preview ---")
        for i, q in enumerate(quiz_questions, 1):
            question_text = list(q.keys())[0]
            answer = "True" if list(q.values())[0] else "False"
            print(f"{i}. {question_text} (Answer: {answer})")

        while True:
            save_choice = input('\nDo you want to save this as the active quiz for students? (y/n): ').lower().strip()
            if save_choice in ['y', 'yes']:
                quiz_path = 'data/quiz.json'
                save_json_file(quiz_path, quiz_questions)
                print("Quiz saved and is now active for students.")
                break
            elif save_choice in ['n', 'no']:
                print("Quiz creation cancelled.")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    @staticmethod
    def add_question_to_bank() -> None:
        """Adds new True/False questions to the question bank."""
        file_path = 'data/questions.json'
        question_bank = load_json_file(file_path)

        while True:
            while True:
                add_more = input('Do you want to add a new question? (y/n): ').lower().strip()
                if add_more in ['y', 'yes']:
                    break
                elif add_more in ['n', 'no']:
                    save_json_file(file_path, question_bank)
                    print("Question bank has been updated.")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")

            question_text = get_valid_string('Enter the new True/False question statement: ')
            print("Is the correct answer True or False?")
            print("1. True")
            print("2. False")
            answer_choice = get_valid_int("Enter your choice: ")

            correct_answer = (answer_choice == 1)
            new_question = {question_text: correct_answer}
            question_bank.append(new_question)
            print("Question added to the bank.")
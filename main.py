# main.py
import person
import student
import teacher
from utils import get_valid_int, get_valid_string

# --- Menus ---
login_menu = """
Select an option:
1. Register
2. Log In
3. Exit
"""

role_selection_menu = """
Are you a:
1. Teacher
2. Student
"""

teacher_menu = """
1. Display Students
2. Divide Students into Groups
3. Create Quiz
4. Add New Question to Bank
5. Exit
"""

student_menu = """
1. Show My Score
2. Take Quiz
3. Exit
"""


def handle_registration():
    """Handles the user registration flow."""
    role_choice = get_valid_int(role_selection_menu)
    match role_choice:
        case 1:
            teacher.Teacher.register()
        case 2:
            student.Student.register()
        case _:
            print('invalid input')


def handle_teacher_session():
    """Manages the interactive session for a logged-in teacher."""
    while True:
        teacher_menu_choice = get_valid_int(teacher_menu)
        match teacher_menu_choice:
            case 1:
                student.Student.display_all_students()
            case 2:
                group_size = get_valid_int('Enter the desired size for each group: ')
                student.Student.divide_students_into_groups(group_size)
            case 3:
                number_of_questions = get_valid_int('How many questions do you want to generate for the quiz? ')
                teacher.Teacher.create_quiz(number_of_questions)
            case 4:
                teacher.Teacher.add_question_to_bank()
            case 5:
                break
            case _:
                print('invalid input')


def handle_student_session(id_number):
    """Manages the interactive session for a logged-in student."""
    while True:
        student_menu_choice = get_valid_int(student_menu)
        match student_menu_choice:
            case 1:
                student.Student.show_score(id_number)
            case 2:
                student.Student.take_quiz(id_number)
            case 3:
                break
            case _:
                print('invalid input')


def handle_login():
    """Handles the user login flow."""
    role_choice = get_valid_int(role_selection_menu)
    match role_choice:
        case 1:  # Teacher Login
            id_number = get_valid_string('Enter ID number: ')
            password = get_valid_string('Enter password: ')
            if teacher.Teacher.log_in(id_number, password):
                handle_teacher_session()

        case 2:  # Student Login
            id_number = get_valid_string('Enter ID number: ')
            password = get_valid_string('Enter password: ')
            if student.Student.log_in(id_number, password):
                handle_student_session(id_number)
        case _:
            print('invalid input')


def main():
    """The main function to run the application's command-line interface."""
    while True:
        login_choice = get_valid_int(login_menu)
        match login_choice:
            case 1:
                handle_registration()
            case 2:
                handle_login()
            case 3:
                print("Exiting program. Goodbye!")
                break
            case _:
                print('invalid input')


if __name__ == "__main__":
    main()
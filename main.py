# main.py
import person
import student
import teacher

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
"""

student_menu = """
1. Show My Score
2. Take Quiz
"""

login_choice = int(input(login_menu))
match login_choice:
    case 1:  # Register
        role_choice = int(input(role_selection_menu))
        match role_choice:
            case 1:
                teacher.Teacher.register()
            case 2:
                student.Student.register()
            case _:
                print('Invalid number entered.')
    case 2:  # Log In
        role_choice = int(input(role_selection_menu))
        match role_choice:
            case 1: # Teacher Login
                id_number = input('Enter ID number: ')
                password = input('Enter password: ')
                if teacher.Teacher.log_in(id_number, password):
                    teacher_menu_choice = int(input(teacher_menu))
                    match teacher_menu_choice:
                        case 1:
                            student.Student.display_all_students()
                        case 2:
                            group_size = int(input('Enter the desired size for each group: '))
                            student.Student.divide_students_into_groups(group_size)
                        case 3:
                            try:
                                number_of_questions = int(input('How many questions do you want to generate for the quiz? '))
                                teacher.Teacher.create_quiz(number_of_questions)
                            except ValueError:
                                print("Invalid input. Please enter a number.")
                            except Exception as e:
                                print(f"An error occurred: {e}")
                        case 4:
                            teacher.Teacher.add_question_to_bank()
                        case _:
                            print('Invalid number entered.')

            case 2: # Student Login
                id_number = input('Enter ID number: ')
                password = input('Enter password: ')
                if student.Student.log_in(id_number, password):
                    student_menu_choice = int(input(student_menu))
                    match student_menu_choice:
                        case 1:
                            student.Student.show_score(id_number)
                        case 2:
                            student.Student.take_quiz(id_number)
                        case _:
                            print('Invalid input.')
    case 3:
        print("Exiting program. Goodbye!")
    case _:
        print('Invalid input.')
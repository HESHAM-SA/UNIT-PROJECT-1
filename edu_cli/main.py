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

teacher_student_menu = """
Are you a:
1. Teacher
2. Student
"""

teacher_menu = """
1. Disply Students
2. Devid class to groubs
3. create Quize
"""

student_menu = """
1. show my scroe
2. solve quize
"""

user_login_choise = int(input(login_menu))
match user_login_choise:
    case 1:
        user_teacher_student_menu = int(input(teacher_student_menu))
        match user_teacher_student_menu:
            case 1:
                teacher.Teacher.register_new_user()
            case 2:
                student.Student.register_new_user()
            case _:
                print('invalid number')
    case 2:
        user_teacher_student_menu = int(input(teacher_student_menu))
        match user_teacher_student_menu:
            case 1:
                id_number = input('Enter id number: ')
                password = input('Enter password: ')
                if teacher.Teacher.log_in(id_number, password):
                    teacher_chose = int(input(teacher_menu))
                    match teacher_chose:
                        case 1:
                            student.Student.display_students()
                        case 2:
                            groups_number = int(input('Enter groups number: '))
                            student.Student.devide_students_groubs(groups_number)
                        case 3:
                            try:
                                number_qustions = int(input('How many qustions you want to genrate? '))
                                teacher.Teacher.create_quize(number_qustions)
                            except Exception as e:
                                print(e)
                        case 4:
                            teacher.Teacher.add_qustion()
                        case _:
                            print('invalid number')

            case 2:
                id_number = input('Enter id number: ')
                password = input('Enter password: ')
                if student.Student.log_in(id_number, password):
                    student_choise = int(input(student_menu))
                    match student_choise:
                        case 1:
                            student.Student.subment_quiz(id_number)
                        case 2:
                            student.Student.subment_quiz(id_number)
                        case _:
                            print('invalid input')

    case _:
        print('invalid input')        
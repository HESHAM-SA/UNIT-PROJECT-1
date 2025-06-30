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
                    print('GOOOOOOOOOOOD Teacher')

            case 2:
                id_number = input('Enter id number: ')
                password = input('Enter password: ')
                if student.Student.log_in(id_number, password):
                    print('GOOOOOOOOOOOD Student')
    case _:
        print('invalid input')
        

        
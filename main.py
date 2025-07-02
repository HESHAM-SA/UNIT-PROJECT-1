import person
import student
import teacher
from utils import get_valid_int, get_valid_string, console
from rich.panel import Panel
from rich.text import Text

# --- Menus ---
login_menu = Text.from_markup(
    """
[#00BFFF]1.[/] Register
[#00BFFF]2.[/] Log In
[#00BFFF]3.[/] Exit
""",
    justify="left",
)

role_selection_menu = Text.from_markup(
    """
[#00BFFF]1.[/] Teacher
[#00BFFF]2.[/] Student
""",
    justify="left",
)

teacher_menu = Text.from_markup(
    """
[#00BFFF]1.[/] Display Students
[#00BFFF]2.[/] Divide Students into Groups
[#00BFFF]3.[/] Create Quiz
[#00BFFF]4.[/] Add New Question to Bank
[#00BFFF]5.[/] Exit
""",
    justify="left",
)

student_menu = Text.from_markup(
    """
[#00BFFF]1.[/] Show My Score
[#00BFFF]2.[/] Take Quiz
[#00BFFF]3.[/] Exit
""",
    justify="left",
)


def handle_registration():
    """Handles the user registration flow."""
    console.print(Panel(role_selection_menu, title="[bold #00BFFF]Select Your Role[/]", border_style="#00BFFF"))
    role_choice = get_valid_int("[bold #FFD700]>>[/] ")
    match role_choice:
        case 1:
            teacher.Teacher.register()
        case 2:
            student.Student.register()
        case _:
            console.print("[bold #FF4500]Invalid input. Please select 1 or 2.[/]")


def handle_teacher_session():
    """Manages the interactive session for a logged-in teacher."""
    while True:
        console.print(Panel(teacher_menu, title="[bold #00BFFF]Teacher Dashboard[/]", border_style="#00BFFF"))
        teacher_menu_choice = get_valid_int("[bold #FFD700]>>[/] ")
        match teacher_menu_choice:
            case 1:
                student.Student.display_all_students()
            case 2:
                group_size = get_valid_int('[bold #FFD700]Enter the desired size for each group: [/]')
                student.Student.divide_students_into_groups(group_size)
            case 3:
                number_of_questions = get_valid_int('[bold #FFD700]How many questions for the quiz? [/]')
                teacher.Teacher.create_quiz(number_of_questions)
            case 4:
                teacher.Teacher.add_question_to_bank()
            case 5:
                break
            case _:
                console.print('[bold #FF4500]Invalid input.[/]')


def handle_student_session(id_number):
    """Manages the interactive session for a logged-in student."""
    while True:
        console.print(Panel(student_menu, title="[bold #00BFFF]Student Dashboard[/]", border_style="#00BFFF"))
        student_menu_choice = get_valid_int("[bold #FFD700]>>[/] ")
        match student_menu_choice:
            case 1:
                student.Student.show_score(id_number)
            case 2:
                student.Student.take_quiz(id_number)
            case 3:
                break
            case _:
                console.print('[bold #FF4500]Invalid input.[/]')


def handle_login():
    """Handles the user login flow."""
    console.print(Panel(role_selection_menu, title="[bold #00BFFF]Select Your Role[/]", border_style="#00BFFF"))
    role_choice = get_valid_int("[bold #FFD700]>>[/] ")
    match role_choice:
        case 1:  # Teacher Login
            id_number = get_valid_string('[bold #FFD700]Enter ID number: [/]')
            password = get_valid_string('[bold #FFD700]Enter password: [/]')
            if teacher.Teacher.log_in(id_number, password):
                handle_teacher_session()

        case 2:  # Student Login
            id_number = get_valid_string('[bold #FFD700]Enter ID number: [/]')
            password = get_valid_string('[bold #FFD700]Enter password: [/]')
            if student.Student.log_in(id_number, password):
                handle_student_session(id_number)
        case _:
            console.print('[bold #FF4500]Invalid input. Please select 1 or 2.[/]')


def main():
    """The main function to run the application's command-line interface."""
    while True:
        console.clear()
        console.print(Panel(login_menu, title="[bold #00BFFF]Welcome to the School CLI[/]", border_style="#00BFFF"))
        login_choice = get_valid_int("[bold #FFD700]>>[/] ")
        match login_choice:
            case 1:
                handle_registration()
            case 2:
                handle_login()
            case 3:
                console.print("[bold #00BFFF]Exiting program. Goodbye![/]")
                break
            case _:
                console.print('[bold #FF4500]Invalid input.[/]')


if __name__ == "__main__":
    main()

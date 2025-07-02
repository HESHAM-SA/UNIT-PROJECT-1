import person
import random
from utils import *
from rich.panel import Panel
from rich.text import Text
from rich.table import Table


class Teacher(person.Person):
    def __init__(self, name: str, id_number: str, city: str, password: str, major: str) -> None:
        super().__init__(name, id_number, city, password)
        self.set_major(major)

    def set_major(self, major: str) -> str:
        """Validates and sets the teacher's major."""
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
            console.print(Panel("[bold #00BFFF]New Teacher Registration[/]", expand=False))
            name = get_valid_string('[bold #FFD700]Enter your name: [/]')
            id_number = get_valid_string('[bold #FFD700]Enter your 3-digit ID number: [/]')
            city = get_valid_string('[bold #FFD700]Enter your city: [/]')
            password = get_valid_string('[bold #FFD700]Enter your password (min 3 chars): [/]', 3)
            major = get_valid_string('[bold #FFD700]Enter your major (e.g., math, history, computer): [/]')
            new_teacher = Teacher(name, id_number, city, password, major)
            all_teachers.append(new_teacher.__dict__)
            save_json_file(file_path, all_teachers)
            console.print(f'[bold #32CD32]Registration successful! Welcome, Teacher {name}.[/]')
        except (ValueError, Exception) as e:
            console.print(f"[bold #FF4500]Registration failed: {e}[/]")

    @staticmethod
    def log_in(id_number: str, password: str) -> bool:
        """Logs in a teacher by verifying their ID and password."""
        file_path = 'data/teachers.json'
        teachers = load_json_file(file_path)

        if not teachers:
            console.print("[bold #FF4500]No teacher data found. Please register first.[/]")
            return False

        for teacher in teachers:
            if id_number == teacher.get('id_number') and verify_password(teacher.get('password'), password):
                console.print(f"[bold #32CD32]Welcome, Teacher: {teacher['name']}![/]")
                return True
        console.print('[bold #FF4500]Invalid ID number or password.[/]')
        return False

    @staticmethod
    def create_quiz(number_of_questions: int) -> None:
        """Creates a new quiz from the question bank."""
        bank_path = 'data/questions.json'
        question_bank = load_json_file(bank_path)

        if not question_bank:
            console.print("[bold #FF4500]Question bank is empty. Please add questions first.[/]")
            return

        if len(question_bank) < number_of_questions:
            console.print(f"[bold #FF4500]Error: You requested {number_of_questions} questions, but only {len(question_bank)} are available.[/]")
            return

        selection_menu = Text.from_markup(
            """
[#00FFFF]1.[/] Randomly select questions
[#00FFFF]2.[/] Use the last questions added
            """,
            justify="left",
        )
        console.print(Panel(selection_menu, title="[bold #00BFFF]How to Select Questions?[/]", border_style="#00BFFF"))
        selection_choice = get_valid_int("[bold #FFD700]Enter your choice: [/]")
        quiz_questions = []
        match selection_choice:
            case 1:
                quiz_questions = random.sample(question_bank, number_of_questions)
                console.print("[#32CD32]Selected random questions.[/]")
            case 2:
                quiz_questions = question_bank[-number_of_questions:]
                console.print("[#32CD32]Selected the last questions from the bank.[/]")
            case _:
                print('invalid input')

        table = Table(title="[bold #00BFFF]Generated Quiz Preview[/]", show_lines=True, border_style="#00BFFF")
        table.add_column("No.", style="cyan", justify="center")
        table.add_column("Question", style="white")
        table.add_column("Correct Answer", style="magenta", justify="center")

        for i, q in enumerate(quiz_questions, 1):
            question_text = list(q.keys())[0]
            answer = "True" if list(q.values())[0] else "False"
            table.add_row(str(i), question_text, answer)
        console.print(table)

        while True:
            save_choice = console.input('[bold #FFD700]\nDo you want to save this as the active quiz? (y/n): [/]').lower().strip()
            if save_choice in ['y', 'yes']:
                quiz_path = 'data/quiz.json'
                save_json_file(quiz_path, quiz_questions)
                console.print("[bold #32CD32]Quiz saved and is now active for students.[/]")
                break
            elif save_choice in ['n', 'no']:
                console.print("[bold #FF4500]Quiz creation cancelled.[/]")
                break
            else:
                console.print("[bold #FF4500]Please enter 'y' for yes or 'n' for no.[/]")

    @staticmethod
    def add_question_to_bank() -> None:
        """Adds new True/False questions to the question bank."""
        file_path = 'data/questions.json'
        question_bank = load_json_file(file_path)

        while True:
            add_more = console.input('[bold #FFD700]Do you want to add a new question? (y/n): [/]').lower().strip()
            if add_more in ['n', 'no']:
                save_json_file(file_path, question_bank)
                console.print("[bold #32CD32]Question bank has been updated.[/]")
                break
            elif add_more not in ['y', 'yes']:
                console.print("[bold #FF4500]Please enter 'y' for yes or 'n' for no.[/]")
                continue

            question_text = get_valid_string('[bold #FFD700]Enter the new True/False question statement: [/]')
            
            answer_menu = Text.from_markup(
                """
[#00FFFF]1.[/] True
[#00FFFF]2.[/] False
                """,
                justify="left"
            )
            console.print(Panel(answer_menu, title="[bold #00BFFF]Is the correct answer True or False?[/]", border_style="#00BFFF"))
            answer_choice = get_valid_int("[bold #FFD700]Enter your choice: [/]")

            correct_answer = (answer_choice == 1)
            new_question = {question_text: correct_answer}
            question_bank.append(new_question)
            console.print("[bold #32CD32]Question added to the bank.[/]")

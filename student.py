import person
import pandas as pd
import random
import time
from utils import *
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import track


class Student(person.Person):
    def __init__(self, name: str, id_number: str, city: str, password: str, exams: list | None = None) -> None:
        super().__init__(name, id_number, city, password)
        self.exams = exams if exams is not None else []

    @staticmethod
    def register() -> None:
        """Handles the registration process for a new student."""
        file_path = 'data/students.json'
        all_students = load_json_file(file_path)

        try:
            console.print(Panel("[bold #00BFFF]New Student Registration[/]", expand=False))
            name = get_valid_string('[bold #FFD700]Enter your name: [/]')
            id_number = get_valid_string('[bold #FFD700]Enter your 3-digit ID number: [/]')
            city = get_valid_string('[bold #FFD700]Enter your city: [/]')
            password = get_valid_string('[bold #FFD700]Enter your password (min 3 chars): [/]', 3)
            new_student = Student(name, id_number, city, password)
            all_students.append(new_student.__dict__)
            save_json_file(file_path, all_students)
            console.print(f'[bold #32CD32]Registration successful! Welcome, {name}.[/]')
        except (ValueError, Exception) as e:
            console.print(f"[bold #FF4500]Registration failed: {e}[/]")

    @staticmethod
    def log_in(id_number: str, password: str) -> bool:
        """Logs in a student by verifying their ID and password."""
        file_path = 'data/students.json'
        students = load_json_file(file_path)

        if not students:
            console.print("[bold #FF4500]No student data found. Please register first.[/]")
            return False

        for student in students:
            if id_number == student.get('id_number') and verify_password(student.get('password'), password):
                console.print(f"[bold #32CD32]Welcome, {student['name']}![/]")
                return True
        console.print("[bold #FF4500]Invalid ID number or password.[/]")
        return False

    @staticmethod
    def display_all_students() -> None:
        """Displays a list of all registered students, their quiz status, and their scors."""
        students = load_json_file('data/students.json')
        if not students:
            console.print('[bold #FF4500]No student data found.[/]')
            return

        table = Table(title="[bold #00BFFF]Registered Students[/]", show_lines=True, border_style="#00BFFF")
        table.add_column("Student Name", style="white", no_wrap=True)
        table.add_column("Quiz Taken?", style="cyan", justify="center")
        table.add_column("Score", style="cyan", justify="center")
        
        for student in students:
            quiz_taken = "[#32CD32]Yes[/]" if student.get('exams') else "[#FF4500]No[/]"
            score_text = ''
            if student['exams']:
                last_score = student['exams'][-1]
                score = last_score.get('score','')
                score_text = str(score)
            table.add_row(student['name'], quiz_taken, score_text)
        
        console.print(table)


    @staticmethod
    def divide_students_into_groups(group_size: int) -> None:
        """Randomly divides students into groups of a specified size."""
        while True:
            students = load_json_file('data/students.json')
            if not students:
                console.print('[bold #FF4500]Could not find the students.json file.[/]')
                return

            student_names = [student['name'] for student in students]

            if not student_names:
                console.print("[bold #FF4500]There are no students to divide.[/]")
                return
            
            if group_size <= 0:
                console.print("[bold #FF4500]Group size must be a positive number.[/]")
                return

            random.shuffle(student_names)
            groups = [student_names[i: i + group_size] for i in range(0, len(student_names), group_size)]

            table = Table(title="[bold #00BFFF]Student Groups[/]", show_lines=True, border_style="#00BFFF")
            max_group_len = len(groups[0])

            console.clear()
            column_colors = ["cyan", "magenta", "yellow", "green", "blue", "red"]
            # Create columns dynamically with different colors
            for i in range(max_group_len):
                color = column_colors[i % len(column_colors)] 
                table.add_column(f"Group {i+1}", style=color, justify="center")

            for group in groups:
                # Pad the group to match table structure
                row_data = group + [''] * (max_group_len - len(group))
                table.add_row(*row_data) 

            console.print(table)
            
            reshuffle_choice = console.input("\n[bold #FFD700]Do you want to re-shuffle the groups? (y/n): [/]").lower().strip()
            if reshuffle_choice not in ['y', 'yes']:
                break
            

    @staticmethod
    def show_score(id_number: str) -> None:
        """Displays the most recent exam score for a given student."""
        file_path = 'data/students.json'
        all_students = load_json_file(file_path)
        student = next((s for s in all_students if s['id_number'] == id_number), None)

        if not student:
            console.print("[bold #FF4500]Student not found.[/]")
            return

        if not student['exams']:
            console.print("[bold #FFD700]You have not taken any quizzes yet.[/]")
        else:
            last_exam = student['exams'][-1]
            score = last_exam.get('score', 'N/A')
            console.print(f"[bold #00BFFF]Your score on the last quiz was: {score}[/]")


    @staticmethod
    def take_quiz(id_number: str) -> None:
        """Allows a student to take the currently active quiz, preventing retakes."""
        quiz_questions = load_json_file('data/quiz.json')
        all_students = load_json_file('data/students.json')

        if not quiz_questions:
            console.print("[bold #FF4500]No quiz is currently available. Please contact your teacher.[/]")
            return

        if not all_students:
            console.print("[bold #FF4500]Error: Could not find student records.[/]")
            return

        student_index, student = next(
            ((i, s) for i, s in enumerate(all_students) if s['id_number'] == id_number),
            (None, None)
        )

        if not student:
            console.print("[bold #FF4500]Error: Could not find your student record.[/]")
            return

        if student['exams']:
            console.print("[bold #FF4500]\nOur records show you have already completed a quiz. You cannot retake it.[/]")
            return

        console.print(f'[bold #00BFFF]The quiz has {len(quiz_questions)} questions.[/]')
        while True:
            user_ready = console.input('[bold #FFD700]Are you ready to begin? (y/n): [/]').lower().strip()
            if user_ready in ['y', 'yes']:
                break
            elif user_ready in ['n', 'no']:
                console.print("[bold #FF4500]Quiz cancelled.[/]")
                return
            else:
                console.print("[bold #FF4500]Please enter 'y' for yes or 'n' for no.[/]")

        student_score = 0
        final_question_results = []
        
        answer_menu = Text.from_markup("[#00FFFF]1.[/] True\n[#00FFFF]2.[/] False", justify="left")

        console.clear()
        console.print(Panel("[bold #00BFFF]Starting Quiz[/]", expand=False))
        time.sleep(1.5) # Pause for effect

        # --- MODIFICATION START: Screen clearing and answer feedback ---
        for i, question_data in enumerate(quiz_questions, 1):
            console.clear() # Clear the screen for the new question
            question_text = list(question_data.keys())[0]
            correct_answer = list(question_data.values())[0]

            console.print(Panel(f"[bold #00BFFF]Question {i}/{len(quiz_questions)}[/]", expand=False, border_style="#00BFFF"))
            console.print(f"\n[bold #FFD700]Q: {question_text}[/]")
            console.print(Panel(answer_menu, border_style="#00BFFF", expand=False))
            
            user_answer = None
            while True:
                user_choice = get_valid_int("[bold #FFD700]Choose your answer: [/]")
                if user_choice == 1:
                    user_answer = True
                    break
                elif user_choice == 2:
                    user_answer = False
                    break
                else:
                    console.print('[bold #FF4500]Invalid input. Please enter 1 or 2.[/]')
            
            is_correct = (correct_answer == user_answer)
            if is_correct:
                student_score += 1
                console.print("[bold #32CD32]Correct![/]")
            else:
                console.print("[bold #FF4500]Incorrect.[/]")

            final_question_results.append({question_text: is_correct})
            time.sleep(1.5) # Pause to let the user see the result
        # --- MODIFICATION END ---
        
        console.clear()
        console.print(Panel(f"[bold #00BFFF]Quiz Finished![/]\n[bold #32CD32]Your final score is: {student_score}/{len(quiz_questions)}[/]", expand=False, border_style="#32CD32"))
        
        results_table = Table(title="[bold #00BFFF]Quiz Results[/]", show_lines=True, border_style="#00BFFF")
        results_table.add_column("Question", style="white")
        results_table.add_column("Your Result", style="cyan", justify="center")

        for res in final_question_results:
            q_text = list(res.keys())[0]
            q_result = "[#32CD32]Correct[/]" if list(res.values())[0] else "[#FF4500]Incorrect[/]"
            results_table.add_row(q_text, q_result)
        console.print(results_table)

        all_students[student_index]['exams'].append({'score': student_score})
        save_json_file('data/students.json', all_students)
        console.print("[bold #32CD32]Your score has been saved.[/]")

# School CLI Management System

A robust and interactive Command-Line Interface (CLI) application for managing students and teachers, creating quizzes, and tracking student performance. Built with Python and enhanced with the `rich` library for a beautiful and intuitive terminal output.

---

## ✨ Features

This application provides a comprehensive set of features for both teachers and students, managed through a clear and interactive menu system.

### For Teachers:
- **🔒 Secure Registration & Login:** Teachers can create a secure, password-protected account and log in.
- **👨‍🏫 Student Management:** View a list of all registered students and their quiz completion status.
- **🎲 Group Creation:** Randomly divide students into groups of any specified size for classroom activities.
- **📝 Quiz Generation:**
    - Create quizzes by selecting a specific number of questions from a central question bank.
    - Choose to populate quizzes with random questions or the most recently added ones.
    - Preview quizzes before making them active for students.
- **🏦 Question Bank:** Easily add new True/False questions to a persistent question bank stored in a JSON file.

### For Students:
- **🔒 Secure Registration & Login:** Students can register with a unique ID and password.
- **✅ Take Quizzes:** Take the active quiz prepared by the teacher. The system provides real-time feedback for each question.
- **📊 View Scores:** After completing a quiz, students can view their final score and a summary of their results.
- **🚫 Prevent Retakes:** The system ensures that a student can only take a specific quiz once.

### General:
- **🎨 Rich CLI:** Utilizes the `rich` library to create visually appealing tables, panels, and styled text, enhancing the user experience.
- **💾 Data Persistence:** All data (teachers, students, questions, quizzes) is saved locally in JSON files, ensuring persistence between sessions.
- **🔑 Password Hashing:** User passwords are securely hashed using SHA-256 before being stored.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Make sure you have the required Python libraries installed. You can install them using pip:
  ```bash
  pip install rich pandas
  ```

### Installation & Running

1.  **Clone the repository or download the files.**
2.  **Ensure the Python files are in the same directory:**
    - `main.py`
    - `person.py`
    - `student.py`
    - `teacher.py`
    - `utils.py`
3.  **Run the application from your terminal:**
    ```bash
    python main.py
    ```
4.  The application will start, and a `data/` directory will be automatically created to store JSON files as you register users and create content.

---

## 🛠️ Project Structure

The project is organized into several modules for clarity and maintainability:

-   `main.py`: The main entry point of the application. It handles the primary user interface, including the main menu and routing to different user sessions (teacher or student).
-   `person.py`: Defines the base `Person` class, which contains shared attributes and methods for both teachers and students, such as ID and password validation.
-   `teacher.py`: Contains the `Teacher` class, which inherits from `Person`. It includes all functionalities specific to teachers, like creating quizzes and managing students.
-   `student.py`: Contains the `Student` class, which also inherits from `Person`. It handles student-specific actions, such as taking quizzes and viewing scores.
-   `utils.py`: A collection of utility functions used across the project, including input validation, password hashing, and loading/saving JSON data.
-   `data/` (directory): This folder is created automatically to store the application's data:
    -   `teachers.json`: Stores registered teacher data.
    -   `students.json`: Stores registered student data.
    -   `questions.json`: The question bank for quizzes.
    -   `quiz.json`: The currently active quiz.
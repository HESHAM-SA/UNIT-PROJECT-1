import json
import os
import hashlib
from typing import Any
from rich.console import Console

# Initialize a global console object for consistent styling
console = Console()

def load_json_file(filepath: str) -> list | dict:
    """Load JSON data from file with error handling."""
    try:
        with open(filepath, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json_file(filepath: str, data: Any) -> None:
    """Save JSON data to file with directory creation."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)


def get_valid_int(prompt: str) -> int:
    """Get valid integer input with range validation."""
    while True:
        try:
            value = int(console.input(prompt))
            return value
        except ValueError:
            console.print("[bold #FF4500]Please enter a valid number.[/]")


def get_valid_string(prompt: str, min_length: int = 1, is_password: bool = False) -> str:
    """Get valid string input with length validation."""
    while True:
        value = console.input(prompt, password=is_password).strip()
        if len(value) >= min_length:
            return value
        console.print(f"[bold #FF4500]Input must be at least {min_length} character(s) long.[/]")


def hash_password(password: str) -> str:
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(stored_hash: str, password: str) -> bool:
    """Verify password against stored hash."""
    return stored_hash == hash_password(password)

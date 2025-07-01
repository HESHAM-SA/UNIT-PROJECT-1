# utils.py
import json
import os
import hashlib

def load_json_file(filepath):
    """Load JSON data from file with error handling."""
    try:
        with open(filepath, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json_file(filepath, data):
    """Save JSON data to file with directory creation."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)

def get_valid_int(prompt: str):
    """Get valid integer input with range validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_string(prompt, min_length=1):
    """Get valid string input with length validation."""
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        print(f"Input must be at least {min_length} character(s) long.")

def hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    """Verify password against stored hash."""
    return stored_hash == hash_password(password)
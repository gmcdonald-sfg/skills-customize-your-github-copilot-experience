"""
File I/O & Data Persistence Assignment - Starter Code
Mergington High School Computer Science

Instructions:
1. Complete the functions below to work with different file formats
2. Run the program to test your file operations
3. Check that the output files are created correctly
"""

import csv
import json
import os

# ===== TASK 1: Read and Write Text Files =====

def process_text_file(input_file, output_file):
    """
    Read a text file, count words, convert to uppercase, and write to output file
    
    Args:
        input_file: Path to the input text file
        output_file: Path to the output text file
    """
    # TODO: Add your code here
    # 1. Open and read the input file using 'with' statement
    # 2. Count the words in the content
    # 3. Convert content to uppercase
    # 4. Write word count and uppercase content to output file
    pass


def read_file_by_lines(filename):
    """
    Read a file line by line and return a list of lines
    
    Args:
        filename: Path to the file to read
        
    Returns:
        List of lines from the file
    """
    # TODO: Add your code here
    # Read the file line by line and return as a list
    pass


# ===== TASK 2: Work with CSV Files =====

def filter_csv_by_score(input_file, output_file, min_score):
    """
    Read a CSV file of students and filter by minimum score
    
    Args:
        input_file: Path to the input CSV file
        output_file: Path to the output CSV file
        min_score: Minimum score threshold
    """
    # TODO: Add your code here
    # 1. Read the CSV file using csv.DictReader
    # 2. Filter students with scores >= min_score
    # 3. Write filtered results to output CSV file
    pass


def calculate_csv_statistics(filename):
    """
    Calculate average score from a CSV file
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        Dictionary with statistics (average, max, min)
    """
    # TODO: Add your code here
    # 1. Read the CSV file
    # 2. Calculate average, max, and min scores
    # 3. Return results as a dictionary
    pass


# ===== TASK 3: Save and Load JSON Data =====

def save_to_json(data, filename):
    """
    Save a Python dictionary or list to a JSON file
    
    Args:
        data: Python dictionary or list to save
        filename: Path to the JSON file
    """
    # TODO: Add your code here
    # Save data to JSON file with proper indentation (indent=2)
    pass


def load_from_json(filename):
    """
    Load data from a JSON file
    
    Args:
        filename: Path to the JSON file
        
    Returns:
        Loaded Python dictionary or list
    """
    # TODO: Add your code here
    # Load and return data from JSON file
    pass


def create_user_profile(username, email, preferences):
    """
    Create a user profile dictionary and save to JSON
    
    Args:
        username: User's username
        email: User's email
        preferences: Dictionary of user preferences
        
    Returns:
        User profile dictionary
    """
    # TODO: Add your code here
    # 1. Create a dictionary with user information
    # 2. Save it to a JSON file named '{username}_profile.json'
    # 3. Return the dictionary
    pass


# ===== Helper Functions =====

def file_exists(filename):
    """
    Check if a file exists
    
    Args:
        filename: Path to the file
        
    Returns:
        True if file exists, False otherwise
    """
    return os.path.exists(filename)


# ===== Main Program =====

def main():
    """
    Main function to test all file I/O operations
    """
    print("Starting File I/O & Data Persistence Assignment...\n")
    
    # Task 1: Text file operations
    print("Task 1: Processing text files...")
    if file_exists('input.txt'):
        process_text_file('input.txt', 'output.txt')
        print("✓ Text file processed!\n")
    else:
        print("⚠ input.txt not found. Create this file first.\n")
    
    # Task 2: CSV operations
    print("Task 2: Processing CSV files...")
    if file_exists('students.csv'):
        filter_csv_by_score('students.csv', 'high_scores.csv', 90)
        stats = calculate_csv_statistics('students.csv')
        print(f"✓ CSV processed! Statistics: {stats}\n")
    else:
        print("⚠ students.csv not found. Create this file first.\n")
    
    # Task 3: JSON operations
    print("Task 3: Working with JSON data...")
    user_data = {
        "username": "alice_smith",
        "email": "alice@example.com",
        "preferences": {
            "theme": "dark",
            "notifications": True
        },
        "scores": [85, 92, 88, 95]
    }
    save_to_json(user_data, 'user_data.json')
    loaded_data = load_from_json('user_data.json')
    print(f"✓ JSON saved and loaded! User: {loaded_data.get('username', 'N/A')}\n")
    
    print("All file operations complete!")
    print("Check your directory for the generated files.")


if __name__ == "__main__":
    main()

# 📘 Assignment: File I/O & Data Persistence

## 🎯 Objective

Learn to read from and write to files in Python, and work with different file formats including text files, CSV, and JSON to persist data between program runs.

## 📝 Tasks

### 🛠️ Read and Write Text Files

#### Description
Create a program that reads content from a text file, processes it, and writes the results to a new file. Practice opening, reading, writing, and properly closing files.

#### Requirements
Completed program should:

- Read content from an existing text file
- Process the content (e.g., count words, convert to uppercase, or filter lines)
- Write the processed content to a new text file
- Use proper file handling with context managers (`with` statement)
- Handle the case when the file doesn't exist

#### Example Input
```python
# Input file: input.txt
Hello, welcome to Python!
This is a file I/O example.
Let's learn about reading and writing files.
```

```python
# Code to process the file
def process_text_file(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        uppercase_content = content.upper()
    
    with open(output_file, 'w') as file:
        file.write(f"Word Count: {word_count}\n\n")
        file.write(uppercase_content)
```

#### Example Output
```
# Output file: output.txt
Word Count: 14

HELLO, WELCOME TO PYTHON!
THIS IS A FILE I/O EXAMPLE.
LET'S LEARN ABOUT READING AND WRITING FILES.
```


### 🛠️ Work with CSV Files

#### Description
Create functions to read data from a CSV file, perform calculations or filtering, and write results to a new CSV file. Learn to use Python's csv module for structured data.

#### Requirements
Completed program should:

- Read data from a CSV file using the csv module
- Process the data (calculate totals, averages, or filter rows)
- Write results to a new CSV file with appropriate headers
- Handle CSV files with different delimiters

#### Example Input
```python
# Input file: students.csv
Name,Age,Grade,Score
Alice,16,Junior,92
Bob,17,Senior,85
Charlie,16,Junior,88
Diana,15,Sophomore,95
```

```python
import csv

def process_csv(input_file, output_file):
    students = []
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Score']) >= 90:
                students.append(row)
    
    with open(output_file, 'w', newline='') as file:
        fieldnames = ['Name', 'Age', 'Grade', 'Score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
```

#### Example Output
```
# Output file: high_scores.csv
Name,Age,Grade,Score
Alice,16,Junior,92
Diana,15,Sophomore,95
```


### 🛠️ Save and Load JSON Data

#### Description
Create a program that saves Python dictionaries and lists to JSON files and loads them back. This is useful for storing application settings, user data, or configuration.

#### Requirements
Completed program should:

- Convert Python dictionaries/lists to JSON format and save to file
- Load JSON data from file and convert back to Python objects
- Handle nested data structures (lists within dictionaries)
- Format JSON output to be human-readable with proper indentation

#### Example Input
```python
import json

# Data to save
user_data = {
    "username": "alice_smith",
    "email": "alice@example.com",
    "preferences": {
        "theme": "dark",
        "notifications": True
    },
    "scores": [85, 92, 88, 95]
}

# Save to JSON
with open('user_data.json', 'w') as file:
    json.dump(user_data, file, indent=2)

# Load from JSON
with open('user_data.json', 'r') as file:
    loaded_data = json.load(file)
    print(f"Welcome back, {loaded_data['username']}!")
```

#### Example Output
```
# File: user_data.json
{
  "username": "alice_smith",
  "email": "alice@example.com",
  "preferences": {
    "theme": "dark",
    "notifications": true
  },
  "scores": [
    85,
    92,
    88,
    95
  ]
}

# Console output:
Welcome back, alice_smith!
```

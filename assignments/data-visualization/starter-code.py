"""
Data Visualization Assignment - Starter Code
Mergington High School Computer Science

Instructions:
1. Install required libraries: pip install matplotlib plotly pandas
2. Complete the functions below to create visualizations
3. Run the program to generate your charts
"""

import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# ===== TASK 1: Create Basic Charts with Matplotlib =====

def create_line_plot():
    """
    Create a line plot showing temperature trends over a week
    """
    # TODO: Add your code here
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temperatures = [72, 75, 73, 78, 80, 77, 74]
    
    # Create your line plot
    # Add title, labels, and save the figure
    pass


def create_bar_chart():
    """
    Create a bar chart comparing student test scores
    """
    # TODO: Add your code here
    students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    scores = [88, 92, 85, 95, 89]
    
    # Create your bar chart
    # Add title, labels, colors, and save the figure
    pass


def create_scatter_plot():
    """
    Create a scatter plot showing relationship between study hours and grades
    """
    # TODO: Add your code here
    study_hours = [2, 4, 6, 8, 10, 3, 5, 7, 9, 1]
    grades = [65, 75, 82, 88, 95, 70, 78, 85, 92, 60]
    
    # Create your scatter plot
    # Add title, labels, and save the figure
    pass


# ===== TASK 2: Build Interactive Visualizations with Plotly =====

def create_interactive_bar_chart():
    """
    Create an interactive bar chart using plotly
    """
    # TODO: Add your code here
    data = {
        'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones'],
        'Sales': [450, 820, 320, 180, 290],
        'Revenue': [450000, 656000, 192000, 54000, 43500]
    }
    df = pd.DataFrame(data)
    
    # Create interactive bar chart with plotly
    # Add hover information and save as HTML
    pass


def create_interactive_scatter():
    """
    Create an interactive scatter plot with plotly
    """
    # TODO: Add your code here
    data = {
        'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK'],
        'GDP': [21.4, 14.3, 5.1, 3.8, 2.9, 2.8],
        'Population': [331, 1439, 126, 83, 1380, 67],
        'Life_Expectancy': [78.9, 76.9, 84.6, 81.3, 69.7, 81.3]
    }
    df = pd.DataFrame(data)
    
    # Create interactive scatter plot showing GDP vs Life Expectancy
    # Use population for bubble size
    # Save as HTML file
    pass


# ===== Main Program =====

def main():
    """
    Main function to run all visualization tasks
    """
    print("Starting Data Visualization Assignment...\n")
    
    # Task 1: Matplotlib visualizations
    print("Task 1: Creating Matplotlib charts...")
    create_line_plot()
    create_bar_chart()
    create_scatter_plot()
    print("✓ Matplotlib charts complete!\n")
    
    # Task 2: Plotly visualizations
    print("Task 2: Creating Plotly interactive charts...")
    create_interactive_bar_chart()
    create_interactive_scatter()
    print("✓ Plotly charts complete!\n")
    
    print("All visualizations created successfully!")
    print("Check your directory for the generated files.")


if __name__ == "__main__":
    main()

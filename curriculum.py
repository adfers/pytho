"""
Module to handle the Python learning curriculum data.
"""

def get_curriculum_data():
    """Returns a structured representation of the 21-day Python learning curriculum."""
    
    curriculum = [
        {
            "week": 1,
            "title": "Python Basics",
            "days": [
                {
                    "day": 1,
                    "topic": "Variables & Data Types",
                    "resources": [
                        {"name": "W3Schools", "url": "https://www.w3schools.com/python/python_variables.asp"}, 
                        {"name": "Mosh's Video", "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc"}
                    ],
                    "practice": "Write a script to store and print your name, age, and favorite number."
                },
                {
                    "day": 2,
                    "topic": "Operators & Expressions",
                    "resources": [
                        {"name": "Programiz", "url": "https://www.programiz.com/python-programming/operators"}, 
                        {"name": "Corey Schafer's Video", "url": "https://www.youtube.com/watch?v=YAbOiGr83cI"}
                    ],
                    "practice": "Write a calculator that adds, subtracts, multiplies, and divides two numbers."
                },
                {
                    "day": 3,
                    "topic": "If Statements & Conditions",
                    "resources": [
                        {"name": "Real Python", "url": "https://realpython.com/python-conditional-statements/"}, 
                        {"name": "freeCodeCamp Video", "url": "https://www.youtube.com/watch?v=DZwmZ8Usvnk"}
                    ],
                    "practice": "Create a program that checks if a number is positive, negative, or zero."
                },
                {
                    "day": 4,
                    "topic": "Loops (for, while)",
                    "resources": [
                        {"name": "W3Schools Loops", "url": "https://www.w3schools.com/python/python_for_loops.asp"}, 
                        {"name": "CS Dojo Video", "url": "https://www.youtube.com/watch?v=HXNhEYqFo0o"}
                    ],
                    "practice": "Print numbers from 1-10 using a loop. Print even numbers only."
                },
                {
                    "day": 5,
                    "topic": "Functions",
                    "resources": [
                        {"name": "Python Functions (Programiz)", "url": "https://www.programiz.com/python-programming/function"}, 
                        {"name": "Mosh's Video", "url": "https://www.youtube.com/watch?v=BVfCWuca9nw"}
                    ],
                    "practice": "Write a function that takes a number and returns its square."
                },
                {
                    "day": 6,
                    "topic": "Lists & Strings",
                    "resources": [
                        {"name": "W3Schools Lists", "url": "https://www.w3schools.com/python/python_lists.asp"}, 
                        {"name": "Corey Schafer's Video", "url": "https://www.youtube.com/watch?v=W8KRzm-HUcc"}
                    ],
                    "practice": "Reverse a string and find the largest number in a list."
                },
                {
                    "day": 7,
                    "topic": "Mini Project (Basics)",
                    "resources": [
                        {"name": "Use Replit to code", "url": "https://replit.com/languages/python3"}
                    ],
                    "practice": "Build a basic calculator or a number guessing game."
                }
            ]
        },
        {
            "week": 2,
            "title": "Intermediate Python",
            "days": [
                {
                    "day": 8,
                    "topic": "Dictionaries & Sets",
                    "resources": [
                        {"name": "W3Schools Dictionaries", "url": "https://www.w3schools.com/python/python_dictionaries.asp"}, 
                        {"name": "Corey Schafer Video", "url": "https://www.youtube.com/watch?v=daefaLgNkw0"}
                    ],
                    "practice": "Count word frequency in a sentence using a dictionary."
                },
                {
                    "day": 9,
                    "topic": "File Handling",
                    "resources": [
                        {"name": "Programiz", "url": "https://www.programiz.com/python-programming/file-operation"}, 
                        {"name": "Mosh's Video", "url": "https://www.youtube.com/watch?v=Uh2ebFW8OYM"}
                    ],
                    "practice": "Read a file and count how many lines it has."
                },
                {
                    "day": 10,
                    "topic": "Error Handling (try-except)",
                    "resources": [
                        {"name": "Real Python", "url": "https://realpython.com/python-exceptions/"}, 
                        {"name": "freeCodeCamp Video", "url": "https://www.youtube.com/watch?v=NIWwJbo-9_8"}
                    ],
                    "practice": "Create a program that handles division by zero errors."
                },
                {
                    "day": 11,
                    "topic": "Modules (math, random)",
                    "resources": [
                        {"name": "Python Modules Guide", "url": "https://docs.python.org/3/tutorial/modules.html"}, 
                        {"name": "Mosh's Video", "url": "https://www.youtube.com/watch?v=GxCXiCVsRSM"}
                    ],
                    "practice": "Generate a random password using random module."
                },
                {
                    "day": 12,
                    "topic": "OOP Basics (Classes & Objects)",
                    "resources": [
                        {"name": "Real Python", "url": "https://realpython.com/python3-object-oriented-programming/"}, 
                        {"name": "Mosh's Video", "url": "https://www.youtube.com/watch?v=pnhO8UaCgxg"}
                    ],
                    "practice": "Create a Car class with attributes like brand and speed."
                },
                {
                    "day": 13,
                    "topic": "APIs & JSON",
                    "resources": [
                        {"name": "Requests Library (Real Python)", "url": "https://realpython.com/python-requests/"}, 
                        {"name": "Corey Schafer Video", "url": "https://www.youtube.com/watch?v=tb8gHvYlCFs"}
                    ],
                    "practice": "Fetch weather data from an API and display it."
                },
                {
                    "day": 14,
                    "topic": "Mini Project",
                    "resources": [
                        {"name": "Use Replit or Jupyter Notebook", "url": "https://jupyter.org/"}
                    ],
                    "practice": "Build a To-Do List App or Weather App using API."
                }
            ]
        },
        {
            "week": 3,
            "title": "Advanced & Final Project",
            "days": [
                {
                    "day": 15,
                    "topic": "Recap & Debugging",
                    "resources": [
                        {"name": "Use Pythontutor to visualize code execution", "url": "https://pythontutor.com/"}
                    ],
                    "practice": "Debug old programs and improve efficiency."
                },
                {
                    "day": 16,
                    "topic": "Data Structures (Stacks, Queues)",
                    "resources": [
                        {"name": "Real Python", "url": "https://realpython.com/python-data-structures/"}
                    ],
                    "practice": "Implement a simple stack and queue in Python."
                },
                {
                    "day": 17,
                    "topic": "Algorithms (Sorting & Searching)",
                    "resources": [
                        {"name": "Khan Academy", "url": "https://www.khanacademy.org/computing/computer-science/algorithms"}
                    ],
                    "practice": "Implement Bubble Sort and Binary Search."
                },
                {
                    "day": 18,
                    "topic": "Python Libraries (pandas, matplotlib)",
                    "resources": [
                        {"name": "Pandas Docs", "url": "https://pandas.pydata.org/docs/"}, 
                        {"name": "Matplotlib Tutorial", "url": "https://matplotlib.org/stable/tutorials/index.html"}
                    ],
                    "practice": "Read a CSV file using Pandas and create a basic graph."
                },
                {
                    "day": 19,
                    "topic": "Final Project Brainstorming",
                    "resources": [
                        {"name": "Use Google Colab", "url": "https://colab.research.google.com/"}
                    ],
                    "practice": "Plan a final project (Choose from ideas below)."
                },
                {
                    "day": 20,
                    "topic": "Final Project (Day 1)",
                    "resources": [
                        {"name": "Use Replit or Jupyter Notebook", "url": "https://replit.com/languages/python3"}
                    ],
                    "practice": "Build a project like: Password Manager, Budget Tracker, or Simple Game."
                },
                {
                    "day": 21,
                    "topic": "Final Project (Day 2)",
                    "resources": [
                        {"name": "Use Replit or Jupyter Notebook", "url": "https://replit.com/languages/python3"}
                    ],
                    "practice": "Complete your final project and showcase it."
                }
            ]
        }
    ]
    
    return curriculum

def get_additional_tools():
    """Returns the list of additional tools recommended for the learning journey."""
    
    tools = [
        "Online Coding Editors: Replit, Jupyter Notebook, Google Colab",
        "Practice & Challenges: HackerRank, LeetCode",
        "Debugging & Visualization: Python Tutor"
    ]
    
    return tools

def get_days_count():
    """Returns the total number of days in the curriculum."""
    return 21

def get_week_count():
    """Returns the total number of weeks in the curriculum."""
    return 3

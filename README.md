# Readme File

📘 Module 1: Introduction to Python & Setup

Installing Python (Windows, macOS, Linux)
Introduction to IDEs (VS Code, PyCharm, Jupyter)
Writing and running your first Python script
Understanding .py files and the Python interpreter

📗 Module 2: Basic Syntax & Data Types

Learning Outcomes: Understand Python’s core syntax and use fundamental data types.

Topics:

Python syntax and indentation rules
Variables and assignment
Data types:
Strings (str)
Numbers (int, float)
Booleans (True, False)
Type casting and type checking
String formatting and operations

📌 Exercises:

Build a simple calculator
Create a string formatter for logging messages

📘 Module 3: Core Data Structures

Learning Outcomes: Work with built-in data structures to organize and manipulate data.

Topics:

Lists:
Indexing, slicing, appending, removing
Tuples:
Immutable sequences
Dictionaries:
Key-value pairs, accessing/modifying values
Sets:
Unordered collections, unique elements

List/Dict comprehensions

📌 Exercises:
Build a contact book using a dictionary
Create a shopping list manager

📙 Module 4: Conditionals and Loops
Learning Outcomes: Make decisions and repeat actions using control flow.

Topics:
Conditional statements:
if, elif, else
Loops:
for loops (with range, lists, dicts)
while loops
break, continue, pass

📌 Exercises:
Number guessing game
Iterate through nested data and summarize it

📗 Module 5: Functions

Learning Outcomes: Reuse code with functions.
Topics:
Defining and calling functions
Parameters and arguments (positional, keyword, default)
Return values
Scope (local vs global variables)

📌 Exercises:

Build a reusable calculator function
Write a function to validate user input
📕 Module 6: Exception Handling
Learning Outcomes: Handle and recover from runtime errors.
Topics:
Types of errors (SyntaxError, TypeError, etc.)
Try-except blocks
Using else and finally
Raising exceptions manually

📌 Exercises:

Input validation with exception handling
Build a file reader with graceful failure

📘 Module 7: Modules & Packages
Learning Outcomes: Organize code and use external libraries.
Topics:
What are modules and packages?
import, from ... import ..., as alias
Built-in modules (e.g., math, os, random)
Installing and using external libraries with pip

Virtual environments

📌 Exercises:

Use random to simulate a dice game
Install and use requests to call an API

📗 Module 8: Object-Oriented Programming (OOP)
Learning Outcomes: Build reusable components using classes and objects.
Topics:
Defining classes and objects
The __init__ method
Instance vs class variables
Methods
Inheritance and method overriding
Using classes in automation (e.g., Page Object Models)

📌 Exercises:

Build a Car class with behavior
Create a Page Object Model class template (basic automation)

📙 Module 9: File Handling
Learning Outcomes: Read/write data to files (text, CSV, logs).
Topics:
Opening files (open, with)
Reading from a file
Writing/appending to files
Working with CSV and JSON files (basic intro)
Real-world examples:
Logging to a file
Reading test data

📌 Exercises:

Create a simple logger
Read and write user data to a file

# Readme File

Difference Between playwright and pytest-playwright

Playwright
----------
pip install playwright
Core Playwright API

This install playwright core (Including Browser Automation and Bindings) but not the pytest integration


Playwright with Pytest
----------------------
pip install pytest-playwright
Adds pytest integration (fixtures and CLI Supports)
- This install the pytest plugin for Playwright
- Write tests using pytest structure (def test_)
- Use fixture like page, browser, etc without manually launching the browser
- Easily runs the test with pytest commands

pytest is a testing framework for Python --- its used to write simple, scalable and readable test cases.



GIT Configuration
-----------------

1. Install and configure git-scm - https://git-scm.com/downloads - Git-Bash
Basic command - https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html


2. Configure the GitHub Account - github.com

git -v

git config --global user.name "username"

git config --global user.email sam@gmail.com
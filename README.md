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

1. Pytest (Most Common)

Status: Fully supported
Integration: Excellent integration with Playwright
Command-line execution: Yes
Fixtures for browser and context: Built-in with pytest-playwright
Async support: Yes
You can use pytest-playwright plugin to easily manage browsers, contexts, pages, etc.

2. Unittest (Python’s built-in testing framework)

Status: Supported
Integration: Manual setup required (no built-in fixtures)
Command-line execution: Yes
Async support: Requires manual handling with asyncio

3. Behave (For BDD – Behavior Driven Development)

Status: Supported, but not officially maintained by Playwright team
Integration: Manual integration with Playwright
Use case: Gherkin-style BDD tests

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

git add .

git add <filename>

git commit -m "Added Commit Message"

git push origin main


No body push the code directly to main branch 
- We will create a branch - JIRA_9383
- You will make the changes - Linked to JIRA_9383
- You will make sure everything is working as expected
- You will raise - PR - Pull Request - JIRA_9383 ---> main
- QA Manager <Approver> - Compare the changes - Merge the change - Reject the PR with Review comments - QA - Work on Review comment - Raise a PR


Assignement - 24th Sep 
- Everyone should do the GIT setup
- Programs in PY - 
    - Create a array and print all the value of an array
    - Create a Numeric Array and Perform the Addition of all value
    - Create a String Array and Calculate the word count of each word in an Array
    
Assignement - 25th Sep  
    - Create 5 functions -
        - Function 1 - Will take the input user age, user phone number
        validate the phone number(10 Digit)
        - Function 2 - Anagram test, 'silent', 'listen' - if letter are same then display output - Both are anagram
        - Function 3 - Take garbage data - "932489JSNjsjnd&*@334" - Segregate the data - Numeric, Special Char, Small case, Upper case
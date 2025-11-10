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
- Write tests using pytest structure (def test_) - 
    - Filename should be starting with test_
    - Function def test_
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

Locators -
--------

HTML - 

<input type="submit" class="button arc sjand ndsanj ndsan" value="Log In">

TagName
Attribute
Value

--> CSS - Locator
1. If you are aware about ID then the css selector would be - #id
2. If you are aware about class then the css selector would be - .classname
    - If there is blank space fill that with . -- .button.arc.sjand.ndsanj.ndsan
3. If we are aware about tagname and value - Then css selector would be - 
[attribute = "value"] -- [type = "Submit"]
4. If we are aware about tagname attribute and value - Then css selector would be - tagname[attribute="value"] -- input[type='submit']
5. parent -- child -- grandchild -- grandgrandchild
6. ID + TagName -- tagName#idvalue
7. Class + TagName -- tagName.className

For Validating the Locator - https://selectorshub.com/selectorshub/


python - Inbuilt - 

- page.get_by_role() to locate by explicit and implicit accessibility attributes.
- page.get_by_text() to locate by text content.
- page.get_by_label() to locate a form control by associated label's text.
- page.get_by_placeholder() to locate an input by placeholder.
- page.get_by_alt_text() to locate an element, usually image, by its text alternative.
- page.get_by_title() to locate an element by its title attribute.
- page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).


--> Xpath - 

//input[@name='username']

Relative - 
    - // - It start with '//'
    - Xpath inbuilt method
    - If we are aware about tagname, attribute and value - //tagname[@attribute=
    'value']

    - Using AND and OR - 
    - //input[@name="customer.address.street" and @class = 'input']
    - //input[@name="customer.address.street" or @class = 'input']

    - By text content
    - //h2[text()='Generate tests with the Playwright Inspector']
    - //h2[contains(text(),'Generate tests with the Playwright Inspector')]
    - //h2[normalize-space(text())='Generate tests with the Playwright Inspector']

    - By using contains()
    - //h2[contains(@id,'intro')]

    - By using starts-with()
    - //h2[starts-with(@id,'intro')]

    - last()/postition()
    - (//h2[starts-with(@class,'anc')])[last()]
    - (//h2[starts-with(@class,'anc')])[4]
    - (//h2[starts-with(@class,'anc')])[position()=1]

    - Xpath axes

    - Using Parent/Child
    - //div[@class='theme-doc-markdown markdown']/div/h2

    - Using Ancestor/Descendant
    - //div[@class='theme-doc-markdown markdown']/descendant::h3
    - //div[@class='theme-doc-markdown markdown']/ancestor::h3

    - following and preceding
    - sibling


Absolute - 
    - 
    - 





Avoid - /html/body/div[1]/div[3]/div[2]/form/table/tbody/tr[1]/td[2]/input



To have the same dependency --> Based on requirement.txt (pip list)
--> pip install -r requirement.txt

--- Assignment - 7th October --- 

1. Navigate to https://www.saucedemo.com/ and add the product and perform the checkout.

-- Validate the Item Added 
-- Validate the Order Number

--- Assignment - 9th October --- 

- Resolve tests/test_dropdown_demo.py file and make it working


# Autosuggest - https://www.wikipedia.org/

Write any text and log all the autosuggestive and click on any one of based on your input


 - Click on Individual Cross Button of Each Subject - Ref - test_autosuggestion_dropdown2.py

 - https://www.spicejet.com/#sourceautocomplete - Select City from the From and To

 PAGE OBJECT MODEL -
 -----------------

 TEST
 
 PAGES

 UTIL
 
 TESTDATA
 
 CONFTEST.PY
 PYTEST.INI
 REQUIREMENT.TXT



Topics to be discussed on Monday - 
OOPS Concept for Pytest
Collection Concept

Classes and Object
class ClassName:

tests/
    createAPI.py
    readAPI.py
    updateAPI.py
    deleteAPI.py

data/
    createAPI.json
    updateAPI.json

utils/
    api_helper.py
    readOTP.py
    sqldb.py

reports/
    allureReport

conftest.py
pytest.ini
requirement.txt
readme.md

CRUD
----
create 
read
update
delete

POST
PUT
PATCH
GET
DELETE

HTTP Status Code

1XX
2XX 
3XX
4XX
5XX 


Allure Report 
------------
1. pip install allure-pytest
2. pytest --alluredir=allure-results your_test_file.py
3. allure serve allure-results


API Frameowork -
1. Create a booking
2. Get a booking
3. Update a booking
4. Get a booking with updated assertion
5. Partial Update a booking
6. Get a booking with partial updated assertion
7. delete a booking
8. get a booking
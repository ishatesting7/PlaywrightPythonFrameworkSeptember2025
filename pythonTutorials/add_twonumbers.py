# Function to add two numbers
def add_numbers(a, b):
    return a + b
# Example usage
result = add_numbers(5, 3)
print("The sum is:", result)
# Function --- IGNORE ---
x = 10
y = 2.4 # float number
isActive = True
_demo = "This is a demo string"
print(_demo)
y = 20 # reassigning the value of y
PI = 3.14 # constant variable
MAX_USERS = 100 # constant variable
# Naming conventions
# camelCase
x,y,z = 1,2,3
print(x,y,z)

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("The product is:", result)

# Convert the temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit   

result = celsius_to_fahrenheit(25)
print("25 degrees Celsius is equal to", result, "degrees Fahrenheit")
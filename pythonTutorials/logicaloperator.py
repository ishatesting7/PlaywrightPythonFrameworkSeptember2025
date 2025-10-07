# Validate the logical Operator
# Today - I will be sharing 3-4 PDF 
# playwright-pytest

m = "I am new to Python"
n = 10
o = 20
# logical and where both the statement should be true
if n >= 10 and o <= 25:
    print("AND condition is met")
else:
    print("AND condition is not met")

# logical or where any one condition is true - output is true
if n > 10 or o <= 25:
    print("OR condition is met")
else:
    print("OR condition is not met")

# negation -- '!=' - '!'
if not(o==25):
    print("I am in Negation Topic")
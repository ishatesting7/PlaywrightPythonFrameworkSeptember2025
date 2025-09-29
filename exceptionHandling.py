x = 10/1

try:
    
    x = 10/1
    a = 10 + 10
    num = float("asndkjasn")

except ZeroDivisionError:
    print("You can't divide by zero!")
except TypeError:
    print("You can only divide numbers!")
except FileNotFoundError:
    print("The file was not found!")
except ArithmeticError:
    print("Something went wrong!")
else:
    print("Division was successful!")
finally:
    print("Execution completed.")
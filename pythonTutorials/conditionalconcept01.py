print("===========IF===========")

x = 20
if x>9:
    print("The Value of x is greater than 9")

print("===========IFELSE===========")

if x>15:
    print("The Value of x is greater than 15")
else:
    print("The Value of x is less than 15")

print("===========ELIF===========")

if x>19:
    print("The Value of x is greater than 19")
elif x>20:
    print("The Value of x is greater then 20")
else:
    print("The value is incorrect")

print("==========NESTED IF CONDITION============")

if x>10:
    if x % 4 == 0:
        print("X is divisible by 4")
    else:
        print("X is not divisible by 4")
else:
    print("the Value is incorrect")


print("===========TERNARY===========")
m = 20
demoresult = "Number is divisible by 5" if m % 5 == 0 else "Number is not divisible by 5"
print(demoresult)





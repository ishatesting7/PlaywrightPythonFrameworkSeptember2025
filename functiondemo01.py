def demo(demo_arg):
    """A simple demo function that prints the argument passed to it."""
    print(f"Demo argument: {demo_arg}")
    print(42)
    return demo_arg
# Example usage
print(demo("Hello, World!"))
print(demo(100))
print(demo(302.45))
print(demo(True))

def demo2(demoName = "DefaultDemo Name"):
    """A demo function with a default argument."""
    print(f"Demo name: {demoName}")
    return demoName
# Example usage
print(demo2())
print(demo2("Custom Demo Name"))
print(demo2(3.14))
print(demo2(False))

print("================================================")

def demo3(demoArg1, demoArg2, demoArg3 = "DefaultDemo3 Arg"):
    """A demo function with multiple arguments, one of which has a default value."""
    print(f"Demo Argument 1: {demoArg1}")
    print(f"Demo Argument 2: {demoArg2}")
    print(f"Demo Argument 3: {demoArg3}")
    return demoArg1, demoArg2, demoArg3
# Example usage
print(demo3("Arg1", "Arg2"))
print(demo3("Arg1", "Arg2", "Custom Arg3"))
print(demo3(10, 20))
print(demo3(1.1, 2.2, 3.3))
print(demo3(True, False, True))

# Variable-length arguments
def demo4(*args):
    """A demo function that accepts a variable number of arguments."""
    print("Demo4 arguments:", args)
    numbers = [x for x in args if isinstance(x, (int, float))]
    total1 = sum(numbers)
    print("Sum of numeric arguments:", total1)
    return args
# Example usage
print(demo4(1, 2, 3))
demo4("A")
print(demo4(1.1, 2.2, 3.3, 4.4,4.5,560.6,70.7,80.8,90))

# keyword variable-length arguments
def demo5(**kwargs):
    """A demo function that accepts keyword arguments."""
    print("Demo5 keyword arguments:", kwargs)
    total2 = sum(value for value in kwargs.values() if isinstance(value, (int, float)))
    print("Sum of numeric keyword argument values:", total2)
    return kwargs
# Example usage
print(demo5(a=1, b=2, c=3))
demo5(x=10, y=20, z=30)
print(demo5(name="Alice", age=30, height=5.5, weight=130))

def demo6(arg1, arg2=20, *args, **kwargs):
    """A demo function that combines positional, default, variable-length, and keyword arguments."""
    print(f"Arg1: {arg1}")
    print(f"Arg2: {arg2}")
    print("Additional positional arguments:", args)
    print("Keyword arguments:", kwargs)
    return arg1, arg2, args, kwargs
# Example usage
print(demo6(10))
print(demo6(10, 30)) 
print(demo6(10,name="Bob", age=25))
print(demo6(5, 15,"extra1", "extra2",a = 10))  

demosquare = lambda arg: arg * arg 
print(demosquare(5))

demoadd = lambda x, y, z: x + y + z
print(demoadd(10, 20, 30))

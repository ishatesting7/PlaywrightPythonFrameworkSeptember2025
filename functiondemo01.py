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
print(demo2(39,99))
print(demo2(3.14))
print(demo2(False))





# *** SCOPE ***

# Python Scope follows the LEGB (Local, Enclosing Functions Locals, Global,
# Built-in) Rule

# LOCAL SCOPE
print("\nLOCAL SCOPE")

print(lambda x: x**2)  # x is a local variable

# ENCLOSING FUNCTION LOCALS SCOPE
print("\nENCLOSING FUNCTION LOCALS SCOPE")

name = "This is a global name"  # Global Scope


def greetings():
    name = "Sammy"  # name is a EFL variable

    def hello():
        print("Hello " + name)  # Look first for locals scope

    hello()


greetings()

# GLOBAL SCOPE
print("\nGLOBAL SCOPE")

x = 25  # Global Scope


def my_func():
    x = 50  # Local Scope
    return x


print(x)  # Call Global Scope

print(my_func())  # Call Local Scope in my_func()

# BUILT-IN SCOPE
print("\nBUILT-IN SCOPE")

print(len(name))  # len is an example of Python built-in variable names

# GLOBAL KEYWORD
print("\nGLOBAL KEYWORD")

num = 50


def change_num():
    """Function to show how to chnage the global variable."""
    global num  # Allow to change the global variable in the local scope
    num = 1000


print(num)
change_num()
print(num)

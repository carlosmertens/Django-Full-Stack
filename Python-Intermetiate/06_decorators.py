# DECORATORS

# Assign a Function to a Variable


def hello(name="Carlos"):
    return "Hello " + name


print("\n** Call Function")
print(hello())

# Assign
print("\n** Assign Function to a variable")
my_greetings = hello
print(my_greetings())

# Function inside a Function
print("\n** Functions inside a Function")


def helloHello(name="Edgar"):
    print("This is helloHello() function")

    def greet():
        return "String inside greet(), inside helloHello()"

    def welcome():
        return "String inside welcome(), inside helloHello()"

    # Call internal Functions
    # print(greet())
    # print(welcome())
    # print("End of helloHello()\n")

    # Return a Function
    if name == "Carlos":
        return greet
    else:
        return welcome


helloHello()

# Returning Functions
print("\n** Return a Function")
x = helloHello("Carlos")
print(x())

# DECORATORS
print("\n** DECORATORS")


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("func() has been called")

    return wrap_func


def func_needs_decorator():
    print("This Function needs a decorator!!")


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

# Using DECORATOR @
print("** Using DECORATOR @")


@new_decorator
def func_use_decorator():
    print("This Function is using decorator!!")


func_use_decorator()

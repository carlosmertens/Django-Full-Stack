# ** FUNCTIONS **

print("\nFunctions:")


def my_funct(name="there", num="1"):  # Create a function
    """
    Function to print greeting with name

    Args:
        name ([String]): Name provided by user
        num (int): Number to be multiply by 100
    """
    print("Hello {}, we multiply your number".format(name))

    return num*100


# Call function with a name as argument
x = my_funct("Carlos", 2)
print(x)

# FILTER - Object Generator

print("\nFilters:")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_bool(num):
    """
    Function to check even numbers

    Args:
        num (int): Number to check if it is even

    Return: 
        return True if the number is even
    """

    return num % 2 == 0


evens = filter(even_bool, my_list)  # Filter out what even_bool returns true
print(list(evens))

# LAMBDA EXPRESSIONS

print("\nLambda Expression:")

evens2 = filter(lambda num: num % 2 == 0, my_list)
print(list(evens2))

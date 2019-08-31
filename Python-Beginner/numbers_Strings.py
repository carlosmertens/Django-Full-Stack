# NUMBERS

# Integers

print("*** INTEGERS AND FLOATS ***")

# Sum, Multiplication, Division and Division residue (Module%)

a, b = 5, 11
print(a+b, a*b, a/b, b/a, b % a)

# Float Point numbers

print(5*2.5)

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print("I pay taxes: ", my_taxes)

# STRINGS

# Indexing, Slicing

print("*** STRINGS ***")

my_string = "abcdefg"

print(my_string[1])  # Index starts at 0
print(my_string[4:])  # Start at index 4 to the end
print(my_string[:4])  # Stop at index 4 (no included)
print(my_string[2:5])  # Start index 4 and stop at index 5 (not included)
print(my_string[::2])  # Grab every 2 step of the whole string

# Basic Methods

my_name = "carlos mertens"
my_email = "superman@email.com"

print(my_name.upper())  # Opposite .lower
print(my_name.capitalize())
print(my_name.split())
print(my_email.split("@"))

# Print Formatting

print("My Name is {} and my email is {}".format(my_name.split()[0], my_email))

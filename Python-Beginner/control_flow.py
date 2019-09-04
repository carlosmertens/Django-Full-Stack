# ** CONTROL FLOW **

# IF, ELIF AND ELSE

age = 21

if age >= 21:
    print("You can drive alone")
elif age < 16:
    print("You are not allow to drive")
else:
    print("You can drive with supervision")

# FOR LOOPS

# Iterate a List
print("\nIterate a List:")
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Iterate a Dictionary
print("\nIterate a Dictionary:")
my_dict = {"One": 1, "Two": 2, "Three": 3}
for key in my_dict:
    print(key)  # Print keys of the dictionary
    print(my_dict[key])  # Print the values

# Iterate using Methods
print("\nIterate using Methods:")
for values in my_dict.values():  # Replace my_dict.keys to iterate keys
    print(values)

# Iterate a Tuple - Tuple unpacking
print("\nIterate Tuples:")
my_pairs = [(1, 2), (3, 4), (5, 6)]  # Tuples inside a list

for item1, item2 in my_pairs:
    print(item1)
    print(item2)
    print("---")

# WHILE LOOPS

print("\nWhile Loops:")
i = 1
while i < 5:
    print("i is: {}".format(i))
    i += 1

# FOR AND RANGE

print("\nFor and Range:")
list_range = list(range(0, 20, 2))  # range(start, stop, step)
print(list_range)

for i in range(0, 20, 2):
    print(i)

# Note: Range is a generator which save ton of memory

# LIST COMPREHENSION

print("\nList Comprehension:")

x = [1, 2, 3, 4, 5]

# Use List Comprehension to return items from x squares
x_square = [item**2 for item in x]
print(x_square)

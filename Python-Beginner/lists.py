# LISTS

print("*** LISTS ***")

# Create a list - It can hold different type of data
my_list = ["item 1", 2, [3, 3.5], "four", 5, 6]
print("My list is: ", my_list)

# Indexing and Slicing Lists
print("Item 3: ", my_list[2])  # Indexing starts at 0
print("From item 3 on: ", my_list[2:])
nested_list = [1, 2, ["x", "y", "z"]]
print(nested_list[2][1])  # Indexing to get "y"

# Lists are mutable
my_list[0] = 1
print(my_list)

# Methods for Lists
print("The lenght of my list is: ", len(my_list))

my_list.append("Seven")  # Add an item at the end
print(my_list)

list_two = [8, 9]
my_list.extend(list_two)  # Join 2 lists
print(my_list)

item = my_list.pop()  # Remove last item and return it
item_two = my_list.pop(2)  # Pop method can be indexed
print("Item is: ", item)
print("Item 2 is: ", item_two)
print(my_list)

my_list.reverse()  # Reverse items in the list
print(my_list)

my_numbers = [4, 6, 2, 9, 4, 8]
my_numbers.sort()
print(my_numbers)

# List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3 items in list
first_col = [item[0] for item in matrix]
print(first_col)

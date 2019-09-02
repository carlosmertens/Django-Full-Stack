# TUPLES

# Tuples are immutable
# Indexing, slicing Tuples is the same as Lists

# Create a tuple

my_tuple = (1, "two", 3, [3.5, "Four"], 5, True, 4, 3, 2, 1)
print(my_tuple[3])

# SETS

# Unordered collection of unique elements

# Create a Set
my_set = set()

# Add elements
my_set.add(1)
my_set.add("two")
my_set.add(1)  # Add same element
print(my_set)

# Convert tuple to set
tupy = (1, 2, 3, 4, 3, 2, 1)
sety = set(tupy)
print(sety)  # Only unique elements

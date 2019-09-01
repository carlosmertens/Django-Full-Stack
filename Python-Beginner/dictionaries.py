# DICTIONARIES

print("*** DICTIONARIES ***")

# Create Dictionary
my_dict = {"key1": "value1", "key2": 2,
           "key3": {"key3.1": [1, 2, "Catch me!!"]}}
print("My dictionary is: ", my_dict)

# Indexing Dictionary
print("Key 2 holds: ", my_dict["key2"])
print(my_dict["key3"]["key3.1"][2])

# Dictionary is mutable
my_dict["key3"]["key3.1"][2] = "Got it!!"
print(my_dict)

# Add item in the Dictionary
my_dict["key4"] = "value4"
print(my_dict)

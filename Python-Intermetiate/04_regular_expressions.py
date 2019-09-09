# REGULAR EXPRESSIONS

# Start by importing "re" for Reglar Expressions

import re

patterns = ["term1", "term2"]
text = "This is a string with term1, but not the other!"

# Search with re
print("\n** Regular Expression - Search")

for pattern in patterns:
    print("*Serching for: " + pattern)

    if re.search(pattern, text):
        print("Found match!")
    else:
        print("No match found!")

match = re.search("term1", text)
print("** Locations start at:", match.start())  # Print location

# Split with re
print("\nRegular Expression - Split")

email = "username@email.com"
split_at = "@"

print(re.split(split_at, email))

# Find with re
finding = re.findall("t", text)

print(finding)

# Create a function to find patterns with re


def multi_re_find(patterns, phrase):
    """Function to find patterns using Regular Expressions."""

    for idx in patterns:
        print("*Searching for pattern {}".format(idx))
        print(re.findall(idx, phrase))
        print("\n")


test_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
test_patterns = ["sd*",     # s followed by zero or more d's
                 "sd+",          # s followed by one or more d's
                 "sd?",          # s followed by zero or one d's
                 "sd{3}",        # s followed by three d's
                 "sd{2,3}",      # s followed by two to three d's
                 "s[sd]+"
                 ]

multi_re_find(test_patterns, test_phrase)

# Strip punctuations
print("** Strip Punctuation")

test_comment = "This is a string! But it has punctuation. How can we remove it?"
new_patterns = ["[^!.?]+"]

multi_re_find(new_patterns, test_comment)

other_patterns = ["[a-z]+"]  # To find capital letters change to A-Z

multi_re_find(other_patterns, test_comment)

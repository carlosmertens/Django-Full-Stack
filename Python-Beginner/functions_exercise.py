#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps.

#####################
## -- PROBLEM 1 -- ##
#####################


def arrayCheck(nums):
    """
    Function to find a sequence 1, 2, 3.

    Given a list of integers, return True if the sequence of numbers 1, 2, 3
    appears in the list somewhere.

    Args:
        nums (Array): Array of integer
    """

    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True

    return False


# Call and test the function:
# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

print(arrayCheck([1, 1, 2, 1, 2, 3]))

#####################
## -- PROBLEM 2 -- ##
#####################


def stringBits(words):
    """
    Function to skip a letter in the string.

    Given a string, return a new string made of every other character starting
    with the first, so "Hello" yields "Hlo".

    Args:
        words (String): String provided by user
    Return:
        result (String): String with every other character skipped
    """

    result = ""

    for i in range(len(words)):
        if i % 2 == 0:
            result = result + words[i]

    return result


# Call and test function:
# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

print(stringBits('Heeololeo'))

#####################
## -- PROBLEM 3 -- ##
#####################


def end_other(a, b):
    """
    Function to compare two strings ending.

    Given two strings, return True if either of the strings appears at the very
    end of the other string, ignoring upper/lower case differences (in other
    words, the computation should not be "case sensitive").

    Args:
        a (String): String provided by user
        b (String): String Provided by user
    """

    a = a.lower()
    b = b.lower()

    return (a.endswith(a) or b.endswith(b))


# Call and test function:
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
print(end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################


def doubleChar(words):
    """
    Function to repeat the chars.

    Given a string, return a string where for every char in the original, there
    are two chars.

    Args:
        words (String): String provided by user
    Return:
        result (String): String with characters dupplicated
    """

    result = ""

    for char in words:
        result += char*2

    return result

# Call and test function:
# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'


print(doubleChar('Hi-There'))

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!


def no_teen_sum(a, b, c):
    """
    [summary]

    [extended_summary]

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]
    """

    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    """
    [summary]

    [extended_summary]

    Args:
        n (int): [description]
    """

    if n in [13, 14, 17, 18, 19]:
        return 0

    return n


# Call and test function:
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

print(no_teen_sum(2, 13, 15))

#####################
## -- PROBLEM 6 -- ##
#####################


def count_evens(nums):
    """
    Count even numbers.

    Return the number of even integers in the given array.

    Args:
        nums (Array): Array with integers items
    """

    count = 0

    for num in nums:
        if num % 2 == 0:
            count += 1

    return count


# Call and test function:
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0
print(count_evens([10, 3, 5]))

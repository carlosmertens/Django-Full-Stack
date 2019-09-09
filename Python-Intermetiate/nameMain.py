# NAME AND MAIN


def my_function():
    print("my_function() is in nameMain.py")


print("TOP LEVEL: nameMain.py")

if __name__ == "__main__":
    print("nameMain.py is being run directly")
else:
    print("nameMain.py has been imported")

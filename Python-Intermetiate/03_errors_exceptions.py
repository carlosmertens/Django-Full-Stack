# *** ERRORS AND EXCEPTIONS ***

# Try and Except

try:
    # Change w for r or any other mistake to see error
    f = open("03_text_sample.txt", "r")
    f.write("Test... writing to text sample file!")
except:
    print("ERROR: could not find file or read data!")
else:
    print("Success!!!")
    f.close()

print("We passed through the error!!!")

# Try, Except and Finally

try:
    f = open("03_text_sample.txt", w)
    f.write("Test 2 ... for text sample file")
except:
    print("ERROR AGAIN, FIND THE BUG!!!")
finally:
    print("Works always!!!")

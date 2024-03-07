'''

Exercise 10: Read line number 4 from the following file
See:

Read Specific Lines From a File in Python
Python read file
Create a test.txt file and add the below content to it.

test.txt file:
'''

# Solution 1

# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])
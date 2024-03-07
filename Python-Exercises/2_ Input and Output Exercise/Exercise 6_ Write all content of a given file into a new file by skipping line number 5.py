

'''
Exercise 6: Write all content of a given file into a new file by skipping line number 5


Create a test.txt file and add the below content to it.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7
Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7

'''


# Solution 1

new_file = open('test.txt', 'w')

input_number = int(input("Please the number of how many times: "))
skipping_ine = 5

for i in range(input_number):
    input_string_line = input("Please the string Line:") 

    if i == skipping_ine:
        pass
    else:
        new_file.write(input_string_line)



# Solution 2
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()


# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1
        
        



# ''' Study:
# Python file handling
# Python Read file
# Python write file
# '''

# ''' File Handling in Python '''

# ''' Example: Create a new empty text file named ‘sales.txt’'''
# # create a empty text file
# # in current directory
# # fp = open('test_file.txt', 'x')
# # fp.close()

# '''Use access mode w if you want to create and write content into a file.'''
# # create a empty text file
# # fp = open('sales_2.txt', 'w')
# # fp.write('first line')
# # fp.close()


# # Let’s verify our operation result.
# import os
# # list files from a working directory
# print(os.listdir())
# # verify file exist
# print(os.path.isfile('sales_2.txt'))


# # Let’s see the example to create a file for writing using the absolute path.

# # create a text file for writing
# with open(r'E:\pynative\reports\profit.txt', 'w') as fp:
#     fp.write('This is first line')
#     pass


# # Let’s verify result using the absolute path.

# import os

# # list files a directory
# print(os.listdir(r'E:\pynative\reports'))
# # output ['sample.txt', 'sales.txt', 'sales_2.txt' 'profit.txt']

# # verify file exist
# print(os.path.isfile(r'E:\pynative\reports\profit.txt'))
# # output True



# # Example 1: create file if not exists.

# import os

# file_path = r'E:\pynative\account\profit.txt'
# if os.path.exists(file_path):
#     print('file already exists')
# else:
#     # create a file
#     with open(file_path, 'w') as fp:
#         # uncomment if you want empty file
#         fp.write('This is first line')
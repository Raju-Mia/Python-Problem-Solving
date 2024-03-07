'''
Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not

'''


# Solution 1
import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
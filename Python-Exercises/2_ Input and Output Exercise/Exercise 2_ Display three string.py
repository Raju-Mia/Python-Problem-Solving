'''
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James
'''


'''
Hint
Use the sep parameter of the print() function to define the separator symbol between each word.


The separator between the arguments to print() function in Python is space by default (softspace feature) , which can be modified and can be made to any character, integer or string as per our choice. The ‘sep’ parameter is used to achieve the same, it is found only in python 3.x or later. It is also used for formatting the output strings.

#code for disabling the softspace feature 
print('G','F','G', sep='') 

#for formatting a date 
print('09','12','2016', sep='-') 

#another example 
print('pratik','geeksforgeeks', sep='@') 


Output: 

GFG
09-12-2016
pratik@geeksforgeeks
'''



# Solution 1
print('Name', 'Is', 'James', sep='**')
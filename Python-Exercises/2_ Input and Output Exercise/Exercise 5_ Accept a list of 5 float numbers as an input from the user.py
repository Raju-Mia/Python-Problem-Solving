'''
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

'''

# Solution 1
total_float_numbers =int(input("Total float numbers: "))
def float_number_list(n):
    float_list = []
    for i in range(n):
        float_input = float(input("Inter Float number: "))
        float_list.append(float_input)
        
    print(float_list)

float_number_list(total_float_numbers)
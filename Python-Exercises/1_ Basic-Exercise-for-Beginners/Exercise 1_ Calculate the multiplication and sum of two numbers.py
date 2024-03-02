

'''
Exercise 1: Calculate the multiplication and sum of two numbers.
Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:
number1 = 20
number2 = 30
Expected Output:
The result is 600

Given 2:
number1 = 40
number2 = 30
Expected Output:
The result is 70

'''

# Solved

number1 = int(input("First Number: "))
number2 = int(input("Second Number: "))


def multiplication_or_sum(number1, number2):
    multiplication = number1 * number2
    if multiplication <= 1000:
        return multiplication
    else:
        return number1 + number2

result = multiplication_or_sum(number1, number2)
print("The result is ", result)

'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number

'''

'''
Hint--
In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.

The String to Reverse
txt = "Hello World" [::-1]
print(txt)

'''


#Solution 1
int_number = (input("Inter Your number: "))
def PalindromeNumber(int_number):
    reversed_number = int_number[::-1]
    if int_number == reversed_number:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")
    
PalindromeNumber(int_number)
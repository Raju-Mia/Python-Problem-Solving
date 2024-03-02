'''

Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.



'''

# solution 1
input_value = input("inter your number: ")
reverse_value=input_value[::-1]
for i in reverse_value:
    print(i, end=' ')




#Solution 2

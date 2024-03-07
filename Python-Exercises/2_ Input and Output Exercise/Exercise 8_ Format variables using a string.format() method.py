'''

Exercise 8: Format variables using a string.format() method.
Write a program to use string.format() method to format the following three variables as per the expected output
'''

# Solution 1
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))
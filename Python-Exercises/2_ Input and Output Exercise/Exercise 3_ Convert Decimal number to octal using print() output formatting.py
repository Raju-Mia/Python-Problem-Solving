'''
Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10

'''

# solution 1
decimal = int(input('Decimal number: '))
print('%o' % decimal)

# Solution 2
'''Decimal to Octal in Python Using oct()'''
print(oct(8))


# Solution 3
def DecimalToOctal(n):
    octal = 0
    count = 1
    deci = n
    
    while (deci != 0):
    
        # Decimals Remainder is Calculated
        remainder = deci % 8
    
        # Storing the Octalvalue
        octal += remainder * count
    
        # Storing Exponential Value
        count = count * 10
        deci = deci // 8
    
    return octal

print(DecimalToOctal(8))
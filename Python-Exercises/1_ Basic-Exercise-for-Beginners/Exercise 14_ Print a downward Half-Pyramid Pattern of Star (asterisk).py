'''
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*

'''

# Solution 1
n = 10
while n>=1:
    for i in range(n):
        print("*", end='')
    n -= 1
    print('')
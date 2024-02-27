'''
Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

'''



# Soluation 1
user_number = int(input("Inter Your number: "))

for i in range(user_number+1):
    for value in range(i):
        print(i, end='')

    print('')


# soluation 2
i = 1
while i <= (user_number):
    for j in range(i):
        print(i, end='')
    i +=1
    print('')


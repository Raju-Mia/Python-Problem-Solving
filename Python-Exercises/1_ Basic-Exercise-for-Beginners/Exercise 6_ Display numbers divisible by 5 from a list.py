'''
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

'''

# soluation 1
def divisible_number(number_list, divisible_by_number):
    for i in number_list:

        if i % divisible_by_number == 0:
            print(i)

        else:
            pass

list = [10, 20, 33, 46, 55]
n = 5
print(divisible_number(list, n))
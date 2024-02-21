'''
A Very Big Sum
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints


Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015

'''


#Soluation 1 for HackerRank submittion.
def aVeryBigSum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum


if __name__ == "__main__":
    n = int(input()) 
    ar = list(map(int, input().split()))
    result = aVeryBigSum(ar)
    print(result)





# Solution 2 for Myself
number_inputs = int(input("Inter how many number would you calculate: "))
def aVeryBigSum(number_inputs):
    array_list = []
    for i in range(0,number_inputs):
        value_is =int(input("Inter your value: "))
        array_list.append(value_is)

    sum_value = 0
    for sum in array_list:
        sum_value = int(sum) + sum_value

    return sum_value


result = aVeryBigSum(number_inputs)
print(result)




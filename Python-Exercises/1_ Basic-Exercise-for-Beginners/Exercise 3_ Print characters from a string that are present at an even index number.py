'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars
p
n
t
v

'''


# Solved 1 ()
str_is = str(input("Inter the String word: "))
str_len = len(str_is)

print("\n")
print("Printing only even index chars \n")
for index_num in range(0, str_len):
    if index_num % 2 == 0:
        print(str_is[index_num])
    else:
        # print("odd Index characters: ", str_is[index_num])
        pass





# solved: 2
print('\n')
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])




#Solution 2: Using list slicing
print('\n')
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)

'''
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.
'''





# Soluation 1
def remove_chars(word, n):
    new_word = word[n:]
    return new_word


a = remove_chars('pynative', 4)
print("New wrod is: ", a)




# Soluation 2
def remove_chars(word, n):
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

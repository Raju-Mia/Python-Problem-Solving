'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times

'''

#soluation 1 

# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count('Emma'))



# Soluation 2
def count_string(str_x, find_word):
    
    len_of_str = len(str_x.split())
    split_str = str_x.split()

    find_word_count = 0
    for str_x in split_str:
        if str_x == find_word:
            find_word_count += 1

    return find_word_count
    
str_x = "Emma is good developer. Emma is a writer"
find_word = "Emma"
print(count_string(str_x, find_word))
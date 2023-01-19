import math
import string 

#Question 1: Write a function called print_squares() 
#that prints out the square of all integers from 1 to 10 inclusive.

"""
nums is a list with #'s 1-10
nums_squared squares each x in nums 
I believe this is faster than looping
"""

def print_squares():
    nums = [1,2,3,4,5,6,7,8,9,10]
    nums_squared = [x**2 for x in nums] # square each element and store in a new list

#Question 2: Write a function called average() 
#that takes in a list of numbers and returns the average of the numbers. 
#Design your function so that it returns None when an invalid input is passed into the function. 

"""
I looked up a function in python that would check if an element was a numeric
and found .isnumeric() This seemed better to use than isdecimal 
"""
def average(nums):
    nums = [*nums]
    if(len(nums) == 0):
        return 0
    result = [] 
    avg = sum(nums)/len(nums)
    return avg

#Question 3: Write a function called is_prime() that takes in a positive integer 
#and returns True if the number is prime and False otherwise. 
#You can assume that the input will be valid (i.e. a positive integer).

"""
I know there is a more algorithmic way of determining whether #'s 1-3 
that would be pretty obvious however I did not want to get stuck too long on one issue
otherwise, every other number is either a multiple of 2 or 3. 

"""
def is_prime(int):
    if int == 1: 
        return False
    if int == 2 or int == 3:
        return True
    if int % 2 == 0 or int % 3 == 0:
        return False
    else:
        return True
"""
only prime numbers are appended to the result list
"""
def prime_100():
    result = []
    for x in range(100):
        if(is_prime(x) == True):
            result.append(x)
    return result

#Question 4: Write a function called count_letters() 
#that counts the number of occurrences of each letter in a string. 
#The return type should be a dictionary of the form

"""
I found a python function that generates a dictionary of ascii letters from A-Z and just declared the default value to be 0 
Then using the update and count function of each key I was able to loop through all the characters which are split by 
using an * which unpacks the string. 
However since each key would be checked against each character I feel that a faster way to approach this would be a binary search. 
"""
def count_letters(input):
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    toCount = ([*input])
    for key in alphabet: 
        alphabet.update({key : toCount.count(key)})
    return alphabet

"""
A list of vowels is compared to each character in a string. 
Again I do think there are faster ways to do this
"""
def filter_strings(list_of_strings):
    result = []
    vowel = ["a", "e", "i", "o", "u"]
    for i in range(len(list_of_strings)):
        for j in vowel:
            if(j in list_of_strings[i] and len(list_of_strings[i]) > 5):
                result.append(list_of_strings[i])
    return result

"""
I've seen another question using left and right pointers to compare values 
and I would have implented it if I spent more time learning it and working on this
"""
def is_palindrome(number):
    number = str(number)
    reversed_num = number[::-1]
    if(number != reversed_num):
        return False
    else: 
        return True

if __name__ == '__main__':
    print(prime_100())
    #print(count_letters("The quick brown fox jumps over the lazy dog."))
    #print(count_letters("Ali Darwish"))
    #testString = ["apple", "banana", "cherry", "kiwi", "mango", "rhythms"]
    #number = 123454321
    #print(filter_strings(testString))
    #print(is_palindrome(number))
    tester = [1,2,3,4,5,6]
    print(average(tester))

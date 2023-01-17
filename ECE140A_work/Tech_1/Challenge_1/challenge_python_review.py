import math
import string 

#Question 1: Write a function called print_squares() 
#that prints out the square of all integers from 1 to 10 inclusive.

def print_squares():
    nums = [1,2,3,4,5,6,7,8,9,10]
    nums_squared = [x**2 for x in nums] # square each element and store in a new list

#Question 2: Write a function called average() 
#that takes in a list of numbers and returns the average of the numbers. 
#Design your function so that it returns None when an invalid input is passed into the function. 

def average(nums):
    for x in nums:
        if x.isnumeric() == False:
            return None
    if len(nums) == 0:
        return 0

#Question 3: Write a function called is_prime() that takes in a positive integer 
#and returns True if the number is prime and False otherwise. 
#You can assume that the input will be valid (i.e. a positive integer).

def is_prime(int):
    if int == 1: 
        return False
    if int == 2 or int == 3:
        return True
    if int % 2 == 0 or int % 3 == 0:
        return False
    else:
        return True

def prime_100():
    result = []
    for x in range(100):
        if(is_prime(x) == True):
            result.append(x)
    return result

#Question 4: Write a function called count_letters() 
#that counts the number of occurrences of each letter in a string. 
#The return type should be a dictionary of the form

def count_letters(input):
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    toCount = ([*input])
    #toCount = toCount.sort()
    for key in alphabet: 
        alphabet.update({key : toCount.count(key)})
    return alphabet

def filter_strings(list_of_strings):
    result = []
    vowel = ["a", "e", "i", "o", "u"]
    for i in range(len(list_of_strings)):
        for j in vowel:
            if(j in list_of_strings[i] and len(list_of_strings[i]) > 5):
                result.append(list_of_strings[i])
    return result

#def is_palindrome(number):

if __name__ == '__main__':
    #print(prime_100())
    #print(count_letters("The quick brown fox jumps over the lazy dog."))
    #print(count_letters("Ali Darwish"))
    testString = ["apple", "banana", "cherry", "kiwi", "mango", "rhythms"]
    print(filter_strings(testString))
#Question3a How many unique ways can you rearrange the string in Question 1 above?
# Explain in detail the logic of how you obtained your answer: Done in pdf file
from math import factorial
string = "FEOEMCIENRTRN"
def unique_arrangement(string):
    n = len(string)  #numerator, add factorial
    # to check for repeats exist or not we need to count letters and their reoccurrence for that we create a list to store counted letters
    checked_letters = []  # list
    denominator = 1  # to start
    # Now we create a loop to count repetitions starting with an empty list, add letters to it by parsing the string letters one by one
    # # we will count how many times each letter appears,take factorial of that count(even if its just once i.e 1)
    # # and multiply that into the denominator i.e. build it
    for letter in string:
        if letter not in checked_letters:
            count = string.count(letter)
            denominator = denominator * factorial(count)
            checked_letters.append(letter)

    return factorial(n) // denominator

total_ways = unique_arrangement(string)
print(f"Number of Unique Arrangements of FEOEMCIENRTRN = {total_ways}")

#Question3b If the first 8 letters of the string in Question 1 is unchanged, how many possible ways can the string in
#Question 1 be rearranged? Please write all these possible strings
k = 8
fixed_string = string[:k]
remaining_string = string[k:]

new_ways = unique_arrangement(remaining_string)

print("Unique rearrangements of FEOEMCIENRTRN with first 8 fixed =", new_ways)

from itertools import permutations
perm_list = permutations(remaining_string)
unique_strings = set()

for p in perm_list:
    rearranged = fixed_string + "".join(p)
    unique_strings.add(rearranged)

print(f"Actual Possible strings when first 8 letters are fixed: ")

for s in unique_strings:
    print(s)

#Question 3c What is the likelihood that the event explained in (b) occurs?
probability = new_ways / total_ways
print("Likelihood =", probability)

#all explanations are in the pdf

#Question3d Write a Python script that takes as input the string in Question 1, and it outputs four items as shown
#below. Your code should be written in a generic way in such a way that it works for any input string and
#any k value.
#Input 1: String from Question 1
#Input 2: Integer value for the no. of unchanged letters (test with k = 8).
#Solution:
#Ask the user to input a string, not assuming it's a non-unique set by default
#Ask the user for the no. of unchanged letters for fixed and moving rearrangement of the string
from math import factorial
from itertools import permutations

input_string = input('Enter your String: ')
try:
    k = int(input("Enter the no. of unchanged letters: "))
except ValueError:
    print("Invalid input for k. Must be an integer.")
    exit()
#Check for empty or whitespace-only input, throw an error statement and exit
if not input_string.strip():
    print("Error: Input string cannot be empty.Try again.")
    exit()
#Check k, the fixed string part cant be longer than the strong so account for that
if k > len(input_string):
    print("No. of unchanged letters cannot be greater than the total string length")
    exit()


#create a generic function that counts unique arrangements for any string, restricted or not by using our OG permutations and repeats factorial formula
def unique_arrangement(input_string):
    n = len(input_string)  #numerator
    # to check for repeats exist or not we need to count letters and their reoccurrence for that we create a list to store counted letters
    checked_letters = []  # list
    denominator = 1  # to start
    # Now we create a loop to count repetitions starting with an empty list, add letters to it by parsing the string letters one by one
    # # we will count how many times each letter appears,take factorial of that count(even if its just once i.e 1)
    # # and multiply that into the denominator i.e. build it
    for letter in input_string:
        if letter not in checked_letters:
            count = input_string.count(letter)
            denominator = denominator * factorial(count)
            checked_letters.append(letter)

    return factorial(n) // denominator


#Time for the 4 different outputs

#Output1 No. of unique ways input string can be rearranged

total_ways = unique_arrangement(input_string)
print(f"Number of Unique Arrangements of {input_string} = {total_ways}")

#Output 2 No. of unique ways input string can be rearranged if the first k letters are fixed.

remaining_string = input_string[k:]
new_ways = unique_arrangement(remaining_string)
print(f"Unique arrangements with first {k} fixed = {new_ways}")

#Output 3
fixed_string = input_string[:k]
perm_list = permutations(remaining_string)
unique_strings = set()

for p in perm_list:
    rearranged = fixed_string + "".join(p)
    unique_strings.add(rearranged)

print(f"Actual Possible strings when first k letters are fixed: ")

for s in unique_strings:
    print(s)

# OUTPUT 4 Probability that the event in Output2 and 3 is realized

probability = new_ways / total_ways

print("Probability =", probability)

#above should work for any string, repeats or not,
#tested FEOEMCIENRTRN answer is 259459200 - correct per the original question 1
#tested FEOEMCIENRTRN with first 8 fixed, answer is 30 - works!
#tested cat, answer is 6 , 3! unique set, 3*2*1 = 6 , works!
#tested braddyy,not unique, 7!/4 = 5040/4 = 1260 correct, works!
#tested probability of if nothing changes event always happens, in case of CAT nothing fixed, the probability is 1
#tested case where n = k in case of cat, 3 letters all 3 fixed. again only 1 outcome can result in that, so 1/6 0.166 answer, works!
#tested for invalid k , works! exits
#################################################################################################

#Question 2a Represent the letters of this string as a set
string = "FEOEMCIENRTRN"
ST1 = set(string)
print("Set representation (ST1)", ST1)

#Question 2b What is the length of this set?
length = len(ST1)
print("Length of Set ", length)

#Question 2b What type of objects do you have in this set?
obj_type = type(next(iter(ST1))).__name__
print("Object type ", obj_type)

#Question 2b What is the domain of this set?
import string
domain = set(string.ascii_uppercase)
print("This is our set ST1:", ST1)
print("This is the Domain:", domain)
print("Is ST1 subset of domain?", ST1.issubset(domain))

#Question 2c Create a new set ST2 of (a), where the letters are now alphabetically ordered.
# Note: Alphabetical ordering doesn't exist in a set, so this would technically be an alp. order of the sequence
ST2 = sorted(ST1)
print("Alphabetically ordered set representation (ST2):", ST2)


#Question2d
#Write a Python script that takes as input the string above but as a SET, and it outputs four items as shown below. Your
#code should be written in a generic way in such a way that it works for any input string
#Solution:
#Ask the user to input a string
input_string = input('Enter your String: ')
#Check for empty or whitespace-only input, throw an error statement and exit
if not input_string.strip():
    print("Error: Input cannot be empty. Try again.")
else:
#Output 1: Set representation (ST1)
    ST1 =  set(input_string)
# using f string in displaying outputs not while variable assignment
    print (f" The Set representation is {ST1}")

    #Output 2: Length of the set
    length = len(ST1)
    print (f" The length of the set is {length}")

    #Output 3: Type of objects in the sequence
    TypeofObjects = type(next(iter(ST1))).__name__
    print (f" The Type of Objects in the set is {TypeofObjects}")

    #Output 4: Alphabetical Set representation (ST2)
    ST2 =  sorted(ST1)
    print (f" The alphabetically ordered Sequence is {ST2}")
#SQ1 = ['F','E','O','E','M','C','I','E','N','R','T','R','N']
#############################################################



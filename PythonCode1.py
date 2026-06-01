#Question 1a Represent the letters of this string as a sequence
string = "FEOEMCIENRTRN"
SQ1 = list(string)
print("Sequence representation (SQ1)", SQ1)

#Question 1b What is the length of this sequence?
length = len(SQ1)
print("Length of Sequence ", length)

#Question 1b What type of objects do you have in this sequence?
obj_type = type(SQ1[0]).__name__
print("Object type ", obj_type)

#Question 1b What is the domain of this sequence?
domain = set(SQ1)
print("Domain:", domain)

#Question 1c Create a new sequence SQ2 of (a), where the letters are now alphabetically ordered.
SQ2 = sorted(SQ1)
print("Alphabetically ordered Sequence representation (SQ2):", SQ2)

#Question1d
#Write a Python script that takes as input the string above, and it outputs four items as shown below. Your
#code should be written in a generic way in such a way that it works for any input string
#Solution
#Ask the user to input a string, input() always returns a string, even if the user enters numbers.
input_string = input('Enter your String: ')
#Check for empty or whitespace-only input, throw an error statement and exit
if not input_string.strip():
    print("Error: Input cannot be empty. Try again.")
else:
    #Output 1: Sequence representation (SQ1)
    SQ1 =  list(input_string)
# using f string in displaying outputs not while variable assignment
    print (f" The Sequence representation is {SQ1}")

#Output 2: Length of the sequence
    length = len(SQ1)
    print (f" The length of Sequence is {length}")

    #Output 3: Type of objects in the sequence
    TypeofCharacter = type(SQ1[0]).__name__
    print (f" The Type of Objects in the Sequence is {TypeofCharacter}")

    #Output 4: Sequence representation (SQ2)
    SQ2 =  sorted(SQ1)
    print (f" The alphabetically ordered Sequence is {SQ2}")
#SQ1 = ['F','E','O','E','M','C','I','E','N','R','T','R','N']
#############################################################
#tested using a few different sequences


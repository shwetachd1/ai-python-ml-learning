print("Hello World!")
#single line comment
x = 5
y = 3
print(x+y)
#multi-line comment select and use ctrl + /
# x = 5
# y = 3
# print(x+y)

import keyword
print(keyword.kwlist)

#cant use a keyword as a variable eg:
# def = 3
# print(def)
#i is square root of -1 is a complex number

#fstring
name = 'PAIDA'
print (name)
semester = 'Fall'
year = 2025
message = f'I enrolled in {name} program starting in {semester} of {year}.'
print (message)

text = 'Sheridan College'
print (f'In Lowercase : {text.lower()}')

#input module
student_name = input('Enter Name')
program_name = input('Enter Program Name')
admission_year = input('Enter Admission Year')
admission_semester = input('Enter Admission Semester')

print(f'\n Hello {student_name} Congrats on being admitted to {program_name} '
      f'in {admission_semester} and {admission_year}.')


import statistics as st
data = [1,2,3,4,5]
(print (st.median(data)))

dtype = type(st.median(data))
print (dtype)

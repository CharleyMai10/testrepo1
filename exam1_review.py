# ISC2310 - Python for Data Analytics
# Instructor's name: Jasser Jasser
# Student's name: <Enter your name here>
# Course section: <Enter course section here>

'''
Exam 1 review
'''

#%%
print('''
Functions we learned so far
''')

print()
input()
int()
float()
str()
bool()
range()
type()
len()


#%%

print('''
Difference between int and float
''')

x = 2
y = 2.9

print(type(x))
print(type(y))

#%%
print(10 / 5)
print(type(10 / 5))

#%%
print('''
Modulus and Quotient
''')
# %%
print(11 % 5)
print(11 // 5)
print(11//3)
# %%
print('''
Operations on numbers and strings
''')

print(100 + 100)
print('100' + '100')

print(100 * 4)
print('100' * 4)

print('100' , 100)

# %%
print('''
Variables naming
''')

print('''
It is always better to name your variable with a name that is related to the program you are solving.
There are rules to naming a variable
1. Must start with a letter
2. May contains letters, numbers, and the underscore character
3. Can't have white spaces
4. Name can't be a keyword (huh!, what is a keyword?)
5. Name is case sensitive
''')

variable = 0
var_ia_ble = 0
_variable = 0
@Variable = 0
0variable = 0

#%%
print('''
----------------------------------------------------------------------------------------------
Escape Sequence                     Meaning
----------------------------------------------------------------------------------------------
\b                                  Backspace
\n                                  Newline
\t                                  Horizontal tab
\\                                  The \ character
\'                                  Single quotation mark
\"                                  Double quotation mark
----------------------------------------------------------------------------------------------
''')

#%%
print('''
Booleans
''')

2 > 5 and ((10 != 10 or 5 >= 5) or .5 <= 1/2)

#%%
print('''
AND Table
-------------------------------------------------------------------------
A                   B                   AND
-------------------------------------------------------------------------
True                True                True
True                False               False
False               True                False
False               False               False
-------------------------------------------------------------------------

OR Table
-------------------------------------------------------------------------
A                   B                   OR
-------------------------------------------------------------------------
True                True                True
True                False               True
False               True                True
False               False               False
-------------------------------------------------------------------------

''')

#%%
print('''
Explain a piece of code.
''')

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("The reverse of the number:",rev)

# %%
print('''
Explain this code...
''')

# Notice that the print() function has a parameter end = ' '
# This parameter means that print() whatever statement to the screen but don't start a new line. Continue on the same line by adding an empty space

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()
# %%

import re

#1. Sequence operations with strings

S = 'Spam'
x = len(S)
print(x)

y = S[0] #The first item in S, indexing by 0 position
print(y)

y = S[-1] #The list item in S
print(y)

y = S[1:] #Everything past the first
print(y)

y = S[0:3] #Everything but the last
print(y)

print(S + 'xyz') #Concentanation

print(S * 8) #Repetition

S = 'shruberry'
L = list(S) #Expand to a list
L[1] = 'c' #Change it in a place
print(''.join(L)) #Join with empty delimeter

#2. Type-specific methods

S = 'Spam'
print(S.find('pa')) #Find the offset of a substring in S
print(S.replace('pa', 'XYZ')) #Replace occurances of a string in S with another

line = 'aaa,bbb,ccc'
print(line.split(',')) #Split on a delimeter to a list of substrings

S = 'spam'
print(S.upper()) #Upper and lowercase conversions
print(S.lower())
print(S.isalpha())

line = 'aaa,bbb,ccc,dd\n'
print(line.rstrip()) #Remove whitepsace characters on the right side
print(line.rstrip().split(','))

print('%s, eggs, and %s' % ('spam', 'SPAM')) #Formatting expression

#Get help with functions
print(dir(S))
help(S.replace)

#3. Other ways to code strings
S = 'A\nB\tC' #\n is end-of-line, \t is a tab
print(len(S)) #Expected output: 5

#Pattern matching

"""This example searches for a substring that begins with the word “Hello,” followed by
zero or more tabs or spaces, followed by arbitrary characters to be saved as a matched
group, terminated by the word “world.”If such a substring is found, portions of the
substring matched by parts of the pattern enclosed in parentheses are available as
groups.
"""

match = re.match('Hello[ \t]*(.*)world', 'Hello   Python world')
print(match.group(1))

#picks out three groups separated by slashes

match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/users/mertkanyener:pyhton_coder')
match.groups()




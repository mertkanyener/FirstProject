import decimal
from fractions import Fraction
#Sets

X = set('spam')
Y = {'h','a','m'}
print(X,Y)
print(X&Y) #intersection
print(X|Y) #union
print(X - Y) #difference
print(X > Y) #superset, returns bool

Z = {n**2 for n in [1,2,3,4]} #set comprehension
print(Z)

result = list(set([1,2,1,3,1])) #filtering out duplicates
print(result)

result = set('spam') - set('ham') #finding differences in collections
print(result)

result = set('spam') == set('asmp')
print(result)

result = 'p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']
print(result)

#Decimals

d = decimal.Decimal('3.141')
d += 1
print(d)

decimal.getcontext().prec = 2
result = decimal.Decimal('1.0') / decimal.Decimal('3.0')
print(result)

#Fractions

f = Fraction(2,3)
f += 1
print(f)

f += Fraction(1,2)
print(f)
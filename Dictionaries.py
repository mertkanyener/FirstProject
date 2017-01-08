#Dictionaries are coded in curly braces and consist of a series of "key:value" pairs

D = {'food' : 'Spam', 'quantity' : 4, 'color' : 'pink'}

print(D['food']) #fetch value of key 'food'

D['quantity'] +=1 #add one to 'quantity' value
print(D)

#Unlike out-of-bounds assignments in lists, which are forbidden, assignments to new dictionary keys create those keys

D = {}

D['name'] = 'Mertkan'
D['job'] = 'Computer engineer'
D['age'] = 22

print(D)

#Note: indexing a dictionary by key is often the fastest way to code a search in Python

#Both the following make the same dictionary as the prior example and its equivalent {} literal form

mertkan1 = dict(name = 'Mertkan', job = 'Computer engineer', age = 22)
print(mertkan1)

mertkan2 = dict(zip(['name', 'job', 'age'], ['Mertkan', 'Computer engineer', 22]))
print(mertkan2)

#Nesting

rec = {'name' : {'first' : 'Mertkan', 'last' : 'Yener'},
                 'jobs' : ['dev', 'mgr'],
                 'age' : 21.5}

print(rec['name']) #name's a nested dictionary
print(rec['name']['last']) #index the nested dictionary
print(rec['jobs']) #jobs is a nested list
print(rec['jobs'][-1]) #index the nested list

rec['jobs'].append('janitor') #expand Mertkan's job description in place
print(rec)

#Missing keys: if Tests

D = {'a' : 1, 'b' : 2, 'c' : 3}
D['e'] = 99

print('f' in D)

if not 'f' in D:
    print('missing')

value = D.get('x', 0) #index but with a default
print(value)

value = D['x'] if 'x' in D else 0 #if/else expression form
print(value)

#Sorting keys: for Loops

Ks = list(D.keys()) #unordered keys list
print(Ks)

Ks.sort() #sorted key list
print(Ks)

for key in Ks: #iterate through the sorted keys
    print(key, '=>', D[key])

#The sorted call returns the result and sorts a variety of object types
#in this case sorting dictionary keys automatically

for key in sorted(D):
    print(key, '=>', D[key])

#page 171



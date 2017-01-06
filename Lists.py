L = [1309, 'mertkan', 3.45]

print(len(L)) #number of items

print(L[:-1]) #slicing the list

print(L[0]) #indexing by position

print(L + [4,5,6])

L.append('something') #add to end of the list
print(L)

L.pop(2) #delete an item in the middle
print(L)

M = ['bb', 'cc', 'aa']
M.sort()
print(M)

M = [[1,2,3], [4,5,6], [7,8,9]]
print(M[1])
print(M[2][2])



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

col2 = [row[1] for row in M] #collect the items in column 2
print(col2)


col2 = [row[1] + 1 for row in M] #add one to each item in column 2

print(col2)

col2_even = [row[1] for row in M if row[1] % 2 == 0] #filter out odd items
print(col2_even)

diag = [M[i][i] for i in [0,1,2]] #collect a diagonal from matrix
print(diag)

doubles = [c*2 for c in 'spam'] #repeat characters in a string
print(doubles)

list_one = list(range(4))
print(list_one)

list_two = list(range(-6,7,2)) #-6 to +6 by 2
print(list_two)

list_three = [[x ** 2, x ** 3] for x in range(4)] #Multiple values
print(list_three)

list_four = [[x, x/2, x*2] for x in range(-6,7,2) if x>0] #if filters
print(list_four)

G = (sum(row) for row in M) #create a generator of row sums
result = next(G)
print(result)
result = next(G)
print(result)
result = next(G)
print(result)



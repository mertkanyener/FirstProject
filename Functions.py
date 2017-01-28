# A simple function that adds two numbers
def addNumbers (x, y):
    return x + y

result = addNumbers(5,6)
print(result)

def intersect (seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = [1,2,3,4,5]
s2 = [4,5,6,7,8]

print(intersect(s1,s2))

#the global statement
X = 88
def func1():
    global X
    X = 99

func1()
print(X)

#lambda

def func2():
    x = 4
    action = (lambda n: x**n)
    return action
x = func2()
print(x(2)) #prints 16, 4**2

#using nonlocal for changes
def tester(start):
    state = start #each call gets its own state
    def nested(label):
        nonlocal state #remembers state in enclosing scope
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('zero')
F('one')
F('two')

#unpacking arguments
def func3(a,b,c,d): print(a,b,c,d)

args = (1,2,3,4)
func3(*args)

args = {'a':1, 'b':2, 'c':3, 'd':4}
func3(**args)


def echo(*args, **kwargs): print(args,kwargs)

pargs = (3,5)
kargs = {'a':8, 'b':9}

echo(*pargs,**kargs)

#keyword-only funcs

def kwonly (a, *b, c): print(a,b,c)

#kwonly(1,2,3) produces TypeError: missing keyword-only arg
kwonly(1,2,3,4,5,6,77, c=3)




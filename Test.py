name = input("Please enter your name: ")
age = input("Age:")
year = (100 - int(age)) + 2017
print("your name is " + name + " your age is " + age + " you will be 100 years old in " + str(year))

number = int(input("give number"))
if number%2 == 0:
    print("bu çift hacı")
    if number%4==0:
        print("4ün katı")
else:
    print("tek sayı")

a = [3, 6, 90, 0, 4, 45, 7, 2]
yarrak=[]
number = int(input("number gir yarramın bası"))
for x in a:
    if x<number:
        yarrak.append(x)
print(yarrak)


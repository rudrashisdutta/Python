#Enter a 2D tuple named pets, compute the sum of the ages of pets present in the third position of the inner tuples.
tpl1,l1=(),[]
a=int(input("Enter the number of pets:\t"))
for i in range(0,a):
    itpl,il=(),[]
    name=input("Name of the pet:\t")
    il.append(name)
    colour=input("Colour of "+name+":\t")
    il.append(colour)
    age=int(input("Age of "+name+":\t"))
    il.append(age)
    itpl=tuple(il)
    l1.append(itpl)
tpl1=tuple(l1)
sumofage=0
for i in range(0,len(tpl1)):
    sumofage+=tpl1[i][2]
print("Sum of age:\t",sumofage)
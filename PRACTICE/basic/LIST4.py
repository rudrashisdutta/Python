#pop an element in a list
lst,a=[1,2,3,4],int(input("Enter the position:\t"))
if a in range(len(lst)):
    lst.pop(a)
else:
    print("Index does not exist!")
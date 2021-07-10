lst,a=[],int(input("Enter the number of elements you want to store in the list:\t"))
for i in range(0,a):
    w="Enter the element "+str(len(lst)+1)+":\t"
    x=eval(input(w))
    lst.append(x)
searchel=eval(input("Enter an element that you want to search in the entered list:\t"))
if searchel in lst:
    print(searchel," is present in the entered list in the position [",lst.index(searchel),"].",sep="")
else:
    print(searchel,"is not present in the entered list.")
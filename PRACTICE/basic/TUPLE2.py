#input a tuple and create another tuple which contains every third element of original tuple i) using slicing ii) without using slicing
tpl1,tpl2=(),()
l1,l2=[],[]
a=int(input("Enter the number of elements you want to store in the tuple:"))
if a>=3:
    for i in range(0,a):
        w="Enter the element "+str(len(l1)+1)+":\t"
        x=eval(input(w))
        l1.append(x)
    tpl1=tuple(l1)
    for i in range(2,len(tpl1),3):
        l2.append(l1[i:i+3:3])
    tpl2=tuple(l2)
    print("The tuple which contains every third element of the original tuple is",tpl2)
else:
    print("The number of elements you wan to store in the tuple is less than 3, but you need to enter more than 3 elements for the program to work.")
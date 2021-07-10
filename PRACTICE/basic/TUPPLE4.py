#enter a 2D tuple named pets then print the second element of the inner tuple
tpl1,l1=(),[]
a=int(input("Enter the number of tuples you want to store in the main tuple:\t"))
for i in range(0,a):
    itpl,il=(),[]
    at=int(input("Enter the number of elements you want to store in inner tuple "+str(len(l1)+1)+":\t"))
    for j in range(0,at):
        x=input("Enter the element "+str(len(il)+1)+":\t")
        il.append(x)
    itpl=tuple(il)
    l1.append(itpl)
tpl1=tuple(l1)
for i in range(0,len(tpl1)):
    print("Tuple ",i+1,":\t",end="",sep=" ")
    if(len(tpl1[i])>1):
        print(tpl1[i][1])
    else:
        print("Not present.")
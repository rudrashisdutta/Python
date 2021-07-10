#2D tuple and print the inner tuples in increasing order of their lengths
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
l2=list(l1)
for i in range(0,len(l2)):
    large=len(l2[0])
    pos=0
    for j in range(0,len(l2)-i):
        if(large<len(l2[j])):
            large=len(l2[j])
            pos=j
    
    l2[pos],l2[len(l2)-i-1]=l2[len(l2)-i-1],l2[pos]
tpl2=tuple(l2)
print(tpl2)
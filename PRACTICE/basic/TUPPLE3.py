#enter a tuple of words of string and change it to pig latin
tpl1,tpl2,l1,l2=(),(),[],[]
a=int(input("Enter the number of elements you want to store in the tuple:"))
for i in range(0,a):
    x=str(input("Enter the element "+str(len(l1)+1)+":\t"))
    l1.append(x)
    xa=x[1:]+x[0]+"ay"
    l2.append(xa)
if len(l1)!=0:
    tpl2=tuple(l2)
    tpl1=tuple(l1)
    print("The pig latin conversion of",tpl1,"is",tpl2)
    del x,xa,a,i
else:
    print("The tuple has no values.")
del tpl1,tpl2,l1,l2
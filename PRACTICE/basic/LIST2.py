#store the unique elements present in two lists in a third list
lst1,a=[],int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO STORE IN THE LIST1:\t"))
for i in range(0,a):
    i1="Enter element"+str(i+1)+":\t"
    x=int(input(i1))
    lst1.append(x)
lst2,b=[],int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO STORE IN THE LIST2:\t"))
for i in range(0,b):
    i1="Enter element"+str(i+1)+":\t"
    x=int(input(i1))
    lst2.append(x)
l1,l2=lst1+lst2,[]
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if l1[i]==l2[j]:
            break
    else:
        l2.append(l1[i])
print("the unique elements are:",l2)
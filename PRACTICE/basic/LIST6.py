#ek list input lena h usme ek element kitni baar present h woh print krna h aur ek list banana h jisme unique elements present honge dusra list jisme duplicate elements honge
lst1,lst2,lst3=[],[],[]
a=int(input("Enter the number of elements you want to store in the original list:\t"))
for i in range(0,a):
    w="Enter element "+str(len(lst1)+1)+":\t"
    x=eval(input(w))
    lst1.append(x)
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
        if lst1[i]==lst2[j]:
            break
    else:
        lst2.append(lst1[i])
print("Unique elements are:",lst2)
for j in range(0,len(lst2)):
    counter=0
    for i in range(0,len(lst1)):
        if lst2[j]==lst1[i]:
            counter+=1
    print("The number of occurences of",lst2[j],"=",counter)
    if counter>1:
        lst3.append(lst2[j])
print("The elements whose duplicates exist in the list:",lst3)
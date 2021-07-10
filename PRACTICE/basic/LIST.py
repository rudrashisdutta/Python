#Print the 2nd largest element present in a list
lst,a=[],int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT TO STORE IN THE LIST"))
for i in range(0,a):
    i1="Enter element"+str(i+1)
    x=int(input(i1))
    lst.append(x)
lst1=list(lst)
for i in range(0,len(lst)):
    for j in range(0,len(lst)-1-i):
        if lst[j+1]<lst[j]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
largest2=lst[len(lst)-2]
print("2nd largest element in",lst1,"is",largest2)
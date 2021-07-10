#enter a list then make another list of cumulative sum of original list
lst=[]
a=int(input("Enter the number of elements you want to store in the list:\t"))
for i in range(0,a):
    w="Enter the element "+str(len(lst)+1)+":\t"
    x=int(input(w))
    lst.append(x)
cumulative=[]
for i in range(0,len(lst)):
    cumulative.append(0)
    for j in range(0,i+1):
        cumulative[i]+=lst[j]
print("The cmulative list of",lst,"is",cumulative)
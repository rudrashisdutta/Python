#calculate mean of the list of number i) using math header ii)without using math header
import statistics
lst,a=[],int(input("Enter the number of elements you want to store in the list:\t"))
for i in range(0,a):
    w="Enter the element "+str(len(lst)+1)+":\t"
    x=int(input(w))
    lst.append(x)
meanoflstbystat=statistics.mean(lst)
sum=0
for i in range(0,len(lst)):
    sum+=lst[i]
meanoflstwithoustat=sum/len(lst)
print("bystat=",meanoflstbystat,"\nwithou stat",meanoflstwithoustat)
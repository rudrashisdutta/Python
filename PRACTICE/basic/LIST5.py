#remove an element in a list
lst,a=[1,2,3,4,10.0,"100"],input("Enter the position:\t")
if int(a) in lst:
    a=int(a)
elif float(a) in lst:
    a=float(a)
if a in lst:
    lst.remove(a)
else:
    print("Element does not exist does not exist!")
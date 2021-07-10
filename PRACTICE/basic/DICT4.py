#Create a list of all the keys of a dictionary and print them.
D={}
l=[]
key=None
while key!={}:
    print("Number of pairs present in the dictionary:",str(len(D)))
    key=eval(input("Enter the key:\t"))
    if key!={}:
            if type(key) is not tuple and type(key) is not dict:
                val=eval(input("Enter the value for the key"+str(key)+":\t"))
                D[key]=val
            else:
                print("Key cannot be of typle tuple or dict!\nEnter again.")
for ikey in D.keys():
    l.append(ikey)
print("The keys in list format:",l)
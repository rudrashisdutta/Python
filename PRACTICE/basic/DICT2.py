#Count the number of pairs.
counter=0
D={}
key=None
while key!={}:
    key=eval(input("Enter the key "+str(len(D)+1)+":\t"))
    if key!={}:
            if type(key) is not tuple and type(key) is not dict:
                val=eval(input("Enter the value for the key"+str(key)+":\t"))
                D[key]=val
            else:
                print("Key cannot be of typle tuple or dict!\nEnter again.")
for i in D.keys():
    counter+=1
print("The number of key:value pairs in ",counter)
#Print the value for the key "avocados".
D={}
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
if "avocados" in D.keys():
    print("Value of \"avocados\" is",D["avocados"])
else:
    print("\"avocados\" is not present as a key in the entered dictionary.")
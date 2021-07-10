dct={}
a=int(input("Enter the number of pairs you want to add in the dictionary:\t"))
for i in range(0,a):
    key=eval(input("Enter the key "+str(len(dct)+1)+":\t"))
    if type(key) is not tuple and type(key) is not dict:
        val=eval(input("Enter the value for the key"+str(key)+":\t"))
        dct[key]=val
    else:
        i-=1
        print("Key cannot be of typle tuple or dict!\nEnter again.")
for i in dct.keys():
    print(i,":",dct[i])
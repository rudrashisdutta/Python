#Use 3 function to enter and print a dictionary after changing the value of the key "apple" if present.
def printdict(dct={}):
    for i in dct.keys():
        print(i,":",dct[i])
def enterdict(dct={}):
    key=None
    while key!={}:
        print("Number of pairs present in the dictionary:",str(len(D)))
        key=eval(input("Enter the key:\t"))
        if key!={}:
            if type(key) is not tuple and type(key) is not dict:
                val=eval(input("Enter the value for the key "+str(key)+":\t"))
                D[key]=val
            else:
                print("Key cannot be of typle tuple or dict!\nEnter again.")
def change():
    if "apple" in D.keys():
        D["apple"]=1.99
D={}
enterdict(D)
change()
printdict(D)
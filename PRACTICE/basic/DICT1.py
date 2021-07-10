#q1) enter a dictionary {name:number} and print in the following format
#    name : number
#    name : number
"""
dct={}
a=int(input("Enter the number of pairs you want to add in the dictionary:\t"))
for i in range(0,a):
    key=eval(input("Enter the key "+str(len(dct)+1)+":\t"))
    if type(key) is not list and type(key) is not tuple and type(key) is not dict:
        val=eval(input("Enter the value for the key"+key+":\t"))
        
    else:
        i-=1
        print("Key cannot be of typle list, tuple or dict!\nEnter again.")
        """
dct={}
a=int(input("Enter the number of pairs you want to add in the dictionary:\t"))
for i in range(0,a):
    key=str(input("Enter the phone number:\t"))
    val=str(input("Enter the name for phone number"+key+":\t"))
    dct[key]=val
for i in dct.keys():
    print(i,":",dct[i])
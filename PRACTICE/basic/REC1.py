def rev(s,x):
    if x>0:
        print(s[x-1],end="")
        rev(s,x-1)
string=str(input("Enter the str:\t"))
print("word in reverse is:\t",end="")
rev(string,len(string))
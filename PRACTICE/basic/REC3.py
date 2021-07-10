def fibbo(a,b,c,d):
    if d<c:
        a,b=b,a+b
        print(b,end=" ")
        b=fibbo(a,b,c,d+1)
    return b
numb=int(input("Enter the number of fibonacci numbers you want:\t"))
fibbo(0,1,numb,0)
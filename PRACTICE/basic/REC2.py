def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
e=int(input("Enter the first number:\t"))
f=int(input("Enter the second number:\t"))
c=gcd(e,f)
print("GCD=",c)
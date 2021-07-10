import math
sqrt,number=None,None
number=float(input("Enter the number:  "))
sqrt=number**(1/2)
print("Square root of",number,"=",sqrt,"(not using func)")
sqrt=math.sqrt(number)
print("Square root of",number,"=",sqrt,"(using func)")
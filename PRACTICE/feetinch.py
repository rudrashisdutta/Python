feet,inch,centimeter=None,None,None
centimeter=float(input("Enter the length in centimeter:"))
inch=centimeter/2.54
feet=inch//12
inch=inch-float(feet*12.0)
print(feet,inch)
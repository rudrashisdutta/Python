str1=str(input("Enter the string:\t"))
str1=str1.capitalize()
i,l=0,len(str1)
space=" "
while i<l:
    pos=str1.find(space,i,len(str1))
    if pos!=-1:
        i=pos+1
        s1=str1[0:i]
        s2=str1[i:l].capitalize()
        str1=s1+s2
    else:
        break
print(str1)
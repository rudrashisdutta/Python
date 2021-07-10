str1=str(input("Enter the string:\t"))
str1=str1.capitalize()
i,l=0,len(str1)
while i<l:
    if str1[i]==" ":
        part1=part2=alpha=""
        i+=1
        alpha=str1[i]
        alpha=alpha.upper()
        part1=str1[0:i]
        part2=str1[i+1:l]
        str1=part1+alpha+part2
    i+=1
print("=>",str1)
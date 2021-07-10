str1,str2,d=str(input("pehla value ghussaya jaaye pehle:\t")),str(input("doosra value ghussaya jaaye abb:\t")),0
i,l,l2=0,len(str1),len(str2)
while i<l:
    pos=str1.find(str2,i,l)
    if pos!=-1:
        d+=1
        i=pos+l2
    else:
        break
print("number of occurences of",str2,"in",str1,"i equal to",d)
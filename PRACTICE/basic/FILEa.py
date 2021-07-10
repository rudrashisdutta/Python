def passcheck(pas=""):
    i,num,count="",0,0
    for i in pas:
        if i.isalnum() or i=="$" or i=="@" or i=="%":
            if i.isnumeric():
                num+=1
            count+=1
        else:
            break
    else:
        if num>0 and count>7:
            return 1
        else:
            return 0
    return 0
def crrctlst(lst=[]):
    for i in lst:
        lst[lst.index(i)]=i.rstrip()
    return lst
def checkid(uid=""):
    with open("C:\PYTHON\security.txt") as acc:
        sec=acc.readlines()
        sec=crrctlst(sec)
    for i in range(0,len(sec),2):
        if uid==sec[i]:
            return 0
    return 1
def datnodat():
    dat,count=" ",0
    with open("C:\PYTHON\security.txt") as acc:
        dat=acc.readline()
        while dat:
            count+=1
            dat=acc.readline()
    if count>=2:
        return 1
    else:
        return 0
def enterinfo():
    uid=str(input("TYPE:\n\"EXIT\" to exit program\nOR\nEnter the new user id:"))
    if uid!="":
        if uid.upper()!="EXIT":
            if checkid(uid)==1:
                pas=" "
                while pas!="DONE":
                    pas=str(input("TYPE:\n\"EXIT\" to exit program\n\"AGAIN\" to enter the user id agin\nOR\nEnter the password:"))
                    if pas.upper()=="AGAIN":
                        if enterinfo()=="EXIT":
                            return "EXIT"
                    elif pas.upper()!="EXIT":
                        if passcheck(pas)==1:
                            with open("C:\PYTHON\security.txt","a") as acc:
                                if datnodat()==1:
                                    acc.write("\n")
                                acc.write(uid+"\n"+pas)
                                pas="DONE"
                        else:
                            print("Wrong Format for Password.\nShould contain atleast a number and only contain spcl characters '$','@','%' and alphabets.")
                            continue
                    else:
                        return "EXIT"
            else:
                print("USER ID already exists!")
                return 1
        else:
            return "EXIT"
    else:
        print("USER ID cannot be blank.")
        return 1
correct=open("C:\PYTHON\security.txt","a")
correct.close()
while enterinfo()!="EXIT":
    continue
def bs(lst=[],elem=None,i=0):
    if lst[i]==elem:
        return elem+" found at index "+str(i)+" of the list"
    if i<len(lst):
        x=bs(lst,elem,i+1)
    else:
        x="Element not found in the list"
    return x
def enterlist():
    lst=[]
    a=input("TYPE:\n\"STOP\": To stop entering into the list\nOR\nEnter element "+str(len(lst)+1)+":\t")
    while a.upper()!="STOP":
        lst.append(a)
        a=input("TYPE:\n\"STOP\": To stop entering into the list\nOR\nEnter element "+str(len(lst)+1)+":\t")
    return lst
lst=enterlist()
elem=input("Enter the element you want to search in the entered list:\t")
print(bs(lst,elem,0),lst)
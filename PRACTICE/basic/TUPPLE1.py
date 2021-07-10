tpl=(1,2,3,4,5)
a=tpl[1]
print(a)
a=3
lst=list(tpl)
lst[1]=a
tpl=tuple(lst)
print(tpl,min(tpl))
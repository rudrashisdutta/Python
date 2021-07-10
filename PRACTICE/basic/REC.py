def compute(num):
    if num==1:
        return 1
    else:
        return(num+compute(num-1))
last=4
ssum=compute(last)
print("Sum of the series 1 to",last,"is",ssum)
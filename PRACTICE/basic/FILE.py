import sys
with open(r"C:\Users\KIIT\Documents\I LOVE YOU.txt") as fh:
    line1=fh.read()
    line2=fh.read(15)
    sys.stdout.write(line1+"\n")
    sys.stdout.write(line2)
    sys.stderr.write("No errors")

lst=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(lst),2):
    print(lst[i])
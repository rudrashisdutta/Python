a=int(input("Enter the number of rows:  "))
for i in range(a,0,-1):
    for j in range(0,i):
        print("*",end='   ')
    print('\n')
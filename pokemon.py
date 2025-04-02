def  pttern(n):
    if n>10:
        return n
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1 or i==n//2):
                print("*",end="")
            else:
                print("")
n=int(input("enter your number"))
m=pttern(n)
print(m)

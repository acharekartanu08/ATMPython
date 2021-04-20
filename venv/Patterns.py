#1
n=int(input("enter no:"))
s=n*2-2
k=1
for l in range(1,n+1):
    v=65
    for sp in range(s):
        print(" ",end="")
    s=s-2
    if l%2==0:
        for p in range(l):
            print(k,end='   ')
    else:
        for p in range(l):
            print(chr(v+p),end='   ')
    print()
    if l%2==0:
        if k==0:
            k=1
        else:
            k=0

#2
n=int(input("enter no:"))
s=n*2-2
for l in range(1,n+1):
    c=1
    k = 0
    v=64
    for sp in range(s):
        print(" ",end="")
    s=s-2
    for p in range(1,l+1):
        if p%2==0:
            print(k,end="   ")
        else:
            print(chr(v+c),end='   ')
            c=c+1

        if p%2==0:
            if k==0:
                k=1
            else:
                k=0
    print()

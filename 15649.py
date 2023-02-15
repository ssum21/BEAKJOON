import math

a=int(input())
temp=a


if(a==1):
    print('')
else:
    li=[0 for i in range(a+1)]
    li[1]=1
    li[2]=1
    n=2
    while(a!=1):
        if(a%n==0):
            print(n)
            a=a//n
        else:
            for i in range(0,temp+1,n):
                li[i]=1
            while(li[n]==1):
                n=n+1

            
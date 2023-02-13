num=int(input())
li=[0 for i in range(num+2)]
li[0]=1
li[1]=1
li[2]=1


def chin(n):
    if(li[n]!=0):
        return li[n]
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        li[n]=chin(n-1)+chin(n-2)
        return li[n]

print(chin(num)) 

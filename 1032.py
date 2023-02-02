num = int(input())
a=list(input())
length=len(a)

for i in range(1,num):
    temp=input()
    for j in range(length):
        if(a[j]!=temp[j]):
            a[j]='?'

for i in range(length):
    print(a[i], end="")
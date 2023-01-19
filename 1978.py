a=int(input())
tot = 0
b= [0 for i in range(a+2)]
c = [0 for i in range(1001)]

c[0]=1
c[1]=1
for i in range(2, 1001):
    for j in range (i*2, 1001, i):
        c[j]=1

b=input().split()

for i in range(a):
    if(c[int(b[i])]==0):
        tot+=1

print(tot)

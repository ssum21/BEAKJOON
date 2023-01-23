N,M=input().split()
N=int(N)
M=int(M)

c = [0 for i in range(1000001)]

c[0]=1
c[1]=1
for i in range(2, 1000001):
    for j in range (i*2, 1000001, i):
        c[j]=1

for i in range(N,M+1):
    if(c[i]==0):
        print(i)


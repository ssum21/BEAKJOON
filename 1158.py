N, K=input().split()
N=int(N)
K=int(K)

arr=[]
corr=[]
for i in range(1,N+1):
    arr.append(i)

temp=K-1
for i in range(1,N):
    a=(arr.pop(temp))
    temp=(temp+K-1)%len(arr)
    corr.append(a)
corr.append(arr.pop())

print("<", ', '.join(str(i) for i in corr), ">", sep = '')

    






import sys

N,M=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
arr_sum=[]
temp=0
for i in range(N):
    temp+=arr[i]
    arr_sum.append(temp)

for i in range(M):
    J, K=map(int,sys.stdin.readline().split())
    temp=arr_sum[K-1]-arr_sum[J-1]+arr[J-1]
    print(temp)
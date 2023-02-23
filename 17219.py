import sys

point=dict()

N,K=map(int, input().split())

for i in range(N):
    site, pw = input().split()
    point[site]=pw

for j in range(K):
    print(point[input().rstrip()])

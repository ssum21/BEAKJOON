num=int(input())

A=list(map(int, input().split(' ')))
B=list(map(int, input().split(' ')))

A.sort()
B.sort(reverse=True)

agb=0

for i in range(num):
    agb+=A[i]*B[i]

print(agb)
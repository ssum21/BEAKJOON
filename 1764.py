N,M=map(int, input().split())

dX=set()
bX=set()
db=set()
for i in range(N):
    dX.add(input())
for j in range(M):
    temp=input()
    if temp in dX:
        db.add(temp)



print(len(db))
for i in sorted(db):
    print(i)
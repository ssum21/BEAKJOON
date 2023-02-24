import sys
input=sys.stdin.readline

A=input().rstrip()
dic=set()

for i in range(len(A)):
    for j in range(i, len(A)):
        dic.add(A[i:j+1])

print(len(dic))
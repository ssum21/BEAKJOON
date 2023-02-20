import sys

input = sys.stdin.readline

N,M=map(int, input().split())
poname={input().rstrip() : i for i in range(1, N+1)}
reverse_poname = dict(map(reversed, poname.items()))

for j in range(M):
    q=input().rstrip()
    if q in poname.keys():
        print(poname[q])
    else:
        print(reverse_poname[int(q)])
import sys
a = int(input())
b = []

for i in range(a):
    b.append(int(sys.stdin.readline()))

for i in sorted(b):
    print(i)

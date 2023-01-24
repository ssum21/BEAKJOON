import sys
a = int(sys.stdin.readline())

temp=-1
b=[]
t=[]
tot=0

for i in range(a):
    t = sys.stdin.readline()
    t = int(t)
    if(t!=0):
        b.append(t)
    else:
        b.pop()

for i in range(len(b)):
    if(b==[]):
        print(0)
        break
    else:
        tot+=b[i]

print(tot)

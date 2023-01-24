import sys
a = int(sys.stdin.readline())

temp=-1
b=[]
t=[]
tot=[]

for i in range(a):
    t = sys.stdin.readline().split()
    b=t[0]
    if(b=='push'):
        c=t[1]
        tot.append(c)
    elif(b=='pop'):
        if(len(tot)<1):
            print(-1)
        else:
            print(tot.pop(0))
            temp-=1
    elif(b=='size'):
        print(len(tot))
    elif(b=='empty'):
        if(len(tot)<1):
            print(1)
        else:
            print(0)
    elif(b=='front'):
        if(len(tot)<1):
            print(-1)
        else:
            print(tot[0])
    else:
        if(len(tot)<1):
            print(-1)
        else:
            print(tot[len(tot)-1])

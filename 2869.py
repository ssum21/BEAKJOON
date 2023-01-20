import math
A,B,V=input().split()

A=int(A)
B=int(B)
diff=A-B
V=int(V)
H=0
temp=0
H= math.ceil((V-A)/diff)
temp = H+1
print(temp)

'''
A,B,V=input().split()

A=int(A)
B=int(B)
V=int(V)
H=0
temp=0

while(V>H):
    H+=A
    temp+=1
    if(H>=V):
        break
    H-=B

print(temp)
'''
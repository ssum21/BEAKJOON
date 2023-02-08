import sys
num=int(input())

li=[]
li=input().split(' ')

tot=0
temp=0
minu=-1000
count0=0

for i in range(num):
    had=int(li[i])
    temp+=had
    if(had==0):
        count0+=1
    if(had<0 and minu<had):
        minu=had
    if(temp<0):
        temp=0
    if(tot<temp):
        tot=temp

if(tot==0 and count0==0):
    print(minu)
else:
    print(tot)
        
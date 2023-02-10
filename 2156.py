num=int(input())
arr=[]
for i in range(num):
    a=int(input())
    arr.append(a)
arrlen=len(arr)
firstnum=0
lastnum=0
midnum=0

for i in range(arrlen):
    if((i+1)%3==0):
        continue
    else:
        firstnum+=int(arr[i])
        int(arr[i])
        
for i in range(arrlen):
    if((i+2)%3==0):
        continue
    else:
        lastnum+=int(arr[i])

for i in range(arrlen):
    if((i+3)%3==0):
        continue
    else:
        midnum+=int(arr[i])


print(max(midnum, firstnum, lastnum))
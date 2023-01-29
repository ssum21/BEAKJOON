num = int(input())
li=[]

for i in range(num):
    a,b=input().split()
    a=int(a)
    b=int(b)
    li.append([a,b])

li.sort(key = lambda x:x[0])
li.sort(key = lambda x:x[1])

for i in range(num):
    print(li[i][0], li[i][1])
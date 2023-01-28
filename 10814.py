a=int(input())
li = []

for i in range(a):
    b = input().split()
    li.append(b)

li.sort(key = lambda x:int(x[0]))

for j in range(a):
    print(li[j][0],li[j][1])
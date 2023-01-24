# 조금만 수정해서 내일 제출해보자
a=int(input())
li = []

for i in range(a):
    b = input().split()
    li.append([b, len(b)])

li.sort(key = lambda x:x[1])

for j in range(a):
    print(li[j][0])
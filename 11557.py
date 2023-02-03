num = int(input())

for _ in range(num):
    temp = int(input())
    li=[]
    for i in range(temp):
        univ, alchol= input().split()
        li.append([univ, int(alchol)])
    li.sort(key=lambda x:x[1],reverse=True)
    print(li[0][0])

'''
Problem 5635.

Given the birthdays of students in a class, write a program to find the oldest and the youngest.
'''

n = int(input())
li=[]

for i in range(n):
    li.append(list(input().split()))

for i in range(n):
    li[i][1]=int(li[i][1])
    li[i][2]=int(li[i][2])
    li[i][3]=int(li[i][3])

li.sort(key=lambda x:x[1],reverse=True)
li.sort(key=lambda x:x[2],reverse=True)
li.sort(key=lambda x:x[3],reverse=True)

print(li[0][0])
print(li[n-1][0])

'''
li = []
for _ in range(int(input())):
    n, d, m, y = input().split()
    li.append([n, int(d), int(m), int(y)])
li.sort(key=lambda x:(x[3],x[2],x[1]))
print(li[-1][0])
print(li[0][0])
'''
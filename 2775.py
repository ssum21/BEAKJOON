import sys
a = int(input())
b = []

c = [[0 for j in range(16)] for i in range(16)]

for i in range(16):
    c[0][i]=1
    c[i][1]=1

for k in range(1, 16):
    for i in range(1,15):
        temp=0
        for j in range(1,i+1):
            temp+=c[k-1][j]
        c[k][i]=temp


for i in range(a):
    j, k =  [int(sys.stdin.readline()) for i in range(2)]
    print(c[j+1][k])

'''
예시코드

t = int(input())

for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력
'''
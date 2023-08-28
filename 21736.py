import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split())

arr=[]
for _ in range(n):
    arr.append(list(map(str,sys.stdin.readline().rstrip())))

width=0
height=0

for i in range(n):
    for j in range(m):
        if(arr[i][j]=='I'):
            width=i
            height=j
            break



def bfs(x, y, nx, ny):
    #방문 리스트 생성
    visited = [[False]*m for _ in range(n) ]
    #현재 위치(노드)에 방문 처리
    visited[x][y]=True
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([(x,y)])
    global temp
    temp=0
    #큐가 완전히 빌 떄까지 반복
    while queue:
        #큐에 삽입된 순서대로 노드 하나 꺼내기
        (x,y) = queue.popleft()
        #현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]!='X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny]=True
                if(arr[nx][ny]=='P'):
                    temp+=1
    return ['TT', temp] [temp > 0]


print(bfs(width,height,n,m))
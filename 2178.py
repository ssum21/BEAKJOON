import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

arr=[]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().rstrip())))

s_arr=[]

def bfs(x, y):
    q=deque()
    v=[[0]*M for _ in range(N)]

    q.append((x, y))
    v[x][y]=1

    while q:
        ti, tj = q.popleft()
        if (ti, tj) == (N-1, M-1):
            return v[ti][tj]
        
        for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj=ti+di, tj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1:
                q.append((ni, nj))
                arr[ni][nj]=0 # 메모리 초과 방지를 위해 필요한 초기화
                v[ni][nj]=v[ti][tj]+1


ans=bfs(0,0)
print(ans)
def dfs(c):
    ans_dfs.append(c) #방문 노드 추가
    visted[c]=1 #방문 표시

    for n in adj[c]:
        if not visted[n]:
            dfs(n)

def bfs(s):
    q=[]

    q.append(s)
    ans_bfs.append(s)
    visted[s]=1

    while q:
        c=q.pop(0)
        for n in adj[c]:
            if not visted[n]: #방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                visted[n]=1



N, M, V=map(int, input().split())
adj=[[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# [1] 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

visted = [0]*(N+1)
ans_dfs = []
dfs(V)

visted = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
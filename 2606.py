N=int(input())
M=int(input())
V=1

def dfs(c):
    ans_dfs.append(c) #방문 노드 추가
    visted[c]=1 #방문 표시

    for n in adj[c]:
        if not visted[n]:
            dfs(n)

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


print(len(ans_dfs)-1)
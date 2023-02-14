'''Problem
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

input
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''

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
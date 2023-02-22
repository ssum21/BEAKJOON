'''Problem / 23.02.22
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

알고리즘 유형 : hash / dict
풀이 참고 없이 스스로 풀었나요? : O
'''

N, K=map(int, input().split())
M=dict()
S=dict()
tot=0
for _ in range(N):
    M[input()]=1
for _ in range(K):
    if input() in M:
        tot+=1
print(tot)

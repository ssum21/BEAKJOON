'''Problem / 23.02.22
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?

알고리즘 유형 : hash / dict
풀이 참고 없이 스스로 풀었나요? : O
'''

for _ in range(int(input())):
    dic=dict()
    for i in range(int(input())):
        N,K=input().split()
        if K not in dic:
            dic[K] = 1
        else:
            dic[K] +=1
    result=1
    for val in dic.values():
        result *= val+1
    print(result-1)





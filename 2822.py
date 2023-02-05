'''
Problem : Sang-geun is the producer of a quiz show. Participants in this quiz show solve a total of 8 problems. Participants solve each problem, and the number of points awarded for solving the problem is determined by the time and difficulty that elapsed from the time the problem was started. A score of 0 is given if the problem is not solved. A participant's total score is the sum of their five highest scores.
Sang-geun was talking on the phone with his girlfriend for a while, so he wasn't counting the scores of the contestants. Write a program that calculates the total score when a participant's 8 problem scores are given.
'''

temp=[]
num=0
tot=0

for i in range(8):
    num=int(input())
    temp.append([i,num])

temp.sort(key = lambda x:x[1],reverse=True)
tomp=[]

for j in range(5):
    tomp.append(temp[j][0]+1)
    tot+=temp[j][1]

tomp.sort()

print(tot)

for k in range(5):
    print(tomp[k])

'''
score = []
for i in range(8):
    score.append(int(input()))
temp = []
answer = 0
for i in range(5):
    answer += max(score)
    temp.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1
temp.sort()
print(answer)
print(*temp)
'''
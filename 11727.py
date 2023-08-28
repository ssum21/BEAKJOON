import math
import sys

n = int(input())
length = n
m = 0
temp = 1

while(n>=0):
    n-=2
    length-=1
    m+=1
    temp+=(math.comb(length,m)*(2**m))    

print(temp%10007)
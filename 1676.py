'''
Problem : Write a program that counts the number of zeros in N! from the back to the first non-zero number.
input : N is given in the first line. (0 ≤ N ≤ 500)
'''

import math

num=int(input())
temp = str(math.factorial(num))
lengtemp = len(temp)-1
tot=0

for i in range(lengtemp, 0, -1):
    if(temp[i]=='0'):
        tot+=1
    else:
        break

print(tot)

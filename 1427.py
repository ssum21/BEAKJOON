a = input()

b = sorted(a, reverse=True)
result=""
for i in b:
    result+=i

print(result)
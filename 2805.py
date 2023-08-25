wood, total = input().split()
wood = int(wood)
total = int(total)
totalcheck = 0
height = input().split()
for h in range(len(height)):
  height[h] = int(height[h])
maxcut = max(height)
cut = maxcut // 2
while totalcheck != total:
  totalcheck =0
  for i in range(wood):
    maxcut = maxcut //  + 1
    if height[i] > cut:
      totalcheck += height[i] - cut
  if totalcheck > total:
    cut -= maxcut
  elif totalcheck < total:
    cut += maxcut
print(cut)
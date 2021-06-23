import random
n = [random.randint(-100, 100) for x in range(30)]
biggest = max(n)
n.index(biggest)
print(n)
print(biggest)
print(n.index(biggest)+1)
for i in range(29):
  if n[i]<0 and n[i+1]<0:
    print(n[i],n[i+1])
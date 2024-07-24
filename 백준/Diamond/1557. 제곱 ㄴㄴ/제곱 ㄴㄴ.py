def check(x):
  cnt = 0; sq = 0
  q = [(1,-1,1)]
  while q:
    n,i,s = q.pop()
    for j in range(i+1,P):
      n1 = n*prime[j]**2
      if n1>x:
        break
      cnt += x//n1*s
      sq |= int(not x%n1)
      q.append((n1,j,-s))
  return x-cnt,sq

prime = []; visited = [0]*50001
for i in range(2,50001):
  if not visited[i]:
    prime.append(i)
    if i<317:
      for j in range(1,50000//i+1):
        visited[i*j] = 1
P = len(prime)
K = int(input())
x,c = 1<<31,30
while 1:
  k,sq = check(x)
  if k<K:
    x += 1<<c
  elif k>K or k==K and sq:
    x -= 1<<c
  else:
    break
  c -= 1
print(x)
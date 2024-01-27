# 11725 : Find to parent in tree
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(v):
    #print(f"#DFS({v})")
    visited[v]=1
    for i in tree[v]:
        if not visited[i]:
            parent[i]=v
            dfs(i)

n=int(input())
tree=[[] for _ in range(n+1)]
visited=[0]*(n+1)
parent=[-1]*(n+1)

for _ in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

#print(tree)
dfs(1)
print('\n'.join(map(str,parent[2:])))
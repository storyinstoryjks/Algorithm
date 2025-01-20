# https://www.acmicpc.net/problem/1068
# 트리
# 그래프 탐색, DFS

input=__import__('sys').stdin.readline

def dfs(root):
    cnt=0
    child_flag=False
    
    if root!=delete_target:
        for next_node in tree[root]:
            if next_node!=delete_target and not visited[next_node]:
                visited[next_node]=1
                child_flag=True
                cnt+=dfs(next_node)

    return +(not child_flag) or cnt
    #return 1 if not child_flag else cnt

n=int(input())
tree=[[] for _ in range(n)]
visited=[0]*(n)

root=0
for end,start in enumerate([*map(int,input().split())]):
    if start==-1:
        root=end
    else:
        tree[start].append(end)
        tree[end].append(start)

delete_target=int(input())

visited[root]=1
print(dfs(root) if delete_target!=root else 0)
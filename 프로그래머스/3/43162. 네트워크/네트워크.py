from collections import deque

def bfs(root,n,computers,visited):
    q=deque([root])
    
    while q:
        cur_node=q.popleft()
        for next_child in range(n):
            if cur_node!=next_child and computers[cur_node][next_child]==1 and not visited[next_child]:
                visited[next_child]=1
                q.append(next_child)
    
    return visited

def solution(n, computers):
    answer = 0
    visited=[0]*n
    
    for root in range(n):
        if not visited[root]:
            visited[root]=1
            visited=bfs(root,n,computers,visited)
            answer+=1
            
    return answer
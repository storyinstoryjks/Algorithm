# https://www.acmicpc.net/problem/21738
# 얼음깨기 펭귄
# 그래프탐색, 트리

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(start):
    cnt,sum_distance=0,0
    q=deque([(start,0)])
    visited=[0]*(n+1)
    visited[start]=1
    
    while q:
        cur_ice,distance=q.popleft()
        if cnt<2:
            if cur_ice<=s:
                cnt+=1; sum_distance+=distance
        else:
            break
        for next_ice in graph[cur_ice]:
            if visited[next_ice]==0:
                visited[next_ice]=1
                q.append((next_ice,distance+1))
    
    return sum_distance
    

n,s,p=map(int,input().split())
graph=[[] for _ in range(n+1)]

# 그래프 설정 및 지지대 얼음 체크
for _ in range(n-1):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

# 전체 얼음 - 최단경로2개의 총길이 - 펭귄서있는얼음
print(n-bfs(p)-1) # BFS 탐색 시작점은 펭귄 서있는 위치
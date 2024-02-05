# Avoid The Lakes
# https://www.acmicpc.net/problem/1743
"""
풀어본 그래프 탐색 문제 중 쉬운 편에 속한 것 같다.

<BFS vs DFS>
=> 둘다 써도 상관없지만, DFS 선택.
이유 1) 메모리 공간: BFS > DFS
이유 2) 최대 크기를 물어보는 문제: 시간 효율 BFS < DFS

<알고리즘>
1. 이차원 배열 준비.
2. 음식물이고, 방문하지 않은 칸이면 dfs 탐색 시작.
3. 현재 노드의 상하좌우 탐색(=자식노드) 및 '음식물이고, 미방문 노드이면' 해당 자식노드 재귀 호출.
    => 이때, cnt 카운팅 들어감.
    => dfs는 개발자가 설정한 방향을 기준으로 트리의 '최대 깊이'까지 먼저 방문한다.
    => 이후, 백트래킹을 통해 다음 노드들을 탐색하는 방식이다.
    => 즉, "최대 깊이까지 진입한 상태에서" "백트래킹을 통해 " "+1씩 더해나가" "최상위 함수에서 모두 더해진 값 리턴."
    => 정리하자면, 카운팅 방식은 "최대로 들어간 트리의 깊이"를 이용하여, "백트래킹으로 더해나간다"이다.
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(sx,sy):
    global n,m
    visited[sx][sy]=1
    cnt=0
    
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx=sx+dx; ny=sy+dy
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]==1 and visited[nx][ny]==0:
                cnt+=dfs(nx,ny)
    
    return cnt+1
        
n,m,k=map(int,input().split())
graph=[[0]*m for _ in range(n)]
visited=[[0]*m for _ in range(n)]
ans=-1

for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            ans=max(ans,dfs(i,j))

print(ans)
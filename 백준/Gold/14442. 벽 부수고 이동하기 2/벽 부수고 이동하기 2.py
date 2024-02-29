# Break Wall and Move
# https://www.acmicpc.net/problem/14442

"""
Python3 정답자가 아무도 없어서, PyPy3로 제출.

난이도 : 보통~어려움
시간 : 40분

[설계]
1. 어떠한 자료구조를 사용해야 하는가?
=> 시작점, 종료점을 바탕으로 2차원 배열을 순회해야하는 문제.
=> 경로를 물어보는 문제이므로, 미로탐색과 같다.
=> 그러므로, 그래프 자료구조 사용.

2. 그래프의 유형은?
=> 각 좌표들은 정점, 동서남북 이동은 간선이 된다.
=> 각 간선마다 길이가 존재하지 않으므로, 가중치가 없는 그래프이며, 최단경로를 구하는 문제이다.

3. 그래프 탐색은?
=> DFS vs BFS
=> 차이점은 '최적 해를 보장할 수 있는가'
=> 가중치 없는 그래프에서의 최단 경로 문제이다.
=> 어떤 좌표칸에 처음 도달했을때의 경로의 길이보다 다른 경로로 도달한 길이가 더 짧다는 보장이 필요.
=> 그러므로, BFS 선택.

4. 방문 배열 설정?
=> 이부분에서 애를 좀 먹었다.
=> 다음 2가지 경우가 있다.
==> 벽을 뚫은 상태에서 다음칸 도달.(뚫었다면, 몇번 뚫었는가? 0~k)
==> 벽을 뚫지 않은 상태에서 다음칸 도달.
=> 이 모든 상태를 기억하며 다음칸의 방문 처리를 진행해야 한다.
=> 즉, visited[next_x][next_y][벽을 뚫었니? 안뚫었니?]라는 '현재 상태'별로 각각 방문처리를 진행해야함.
=> 그러므로, q의 원소는 (좌표x,좌표y,벽뚫기 여부를 나타내는 현재 상태)가 되어야 한다.
=> k번까지만 뚫을 수 있으므로, 이를 유의.
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(n,m,k,wallCnt):
    q=deque([(0,0,wallCnt)])
    visited[0][0][wallCnt]=1
    
    while q:
        x,y,cnt=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][cnt]
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx=x+dx; ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                # 다음칸이 벽이 아니고, 현재 벽뚫기 상태 기준에서 다음칸 미방문이면
                if graph[nx][ny]=='0' and visited[nx][ny][cnt]==0:
                    q.append((nx,ny,cnt))
                    # 현재 상태 기준의 부모의 경로길이+1
                    visited[nx][ny][cnt]=visited[x][y][cnt]+1
                # 다음칸이 벽이고, '벽을 더 뚫을 수 있고'
                # '벽을 뚫었을 때 기준으로 미방문칸이면'
                if graph[nx][ny]=='1' and cnt!=k and visited[nx][ny][cnt+1]==0:
                    q.append((nx,ny,cnt+1)) # 벽 뚫었기에, 현재상태+1로 갱신.
                    visited[nx][ny][cnt+1]=visited[x][y][cnt]+1
    
    return -1

        
n,m,k=map(int,input().split())
graph=[[*input()][:-1] for _ in range(n)]
# 3차원 방문 배열 설정
# ex) k==2
# [0,0,0] : idx=(0,1,2)=(한번도 안뚫음,1번뚫음,k번뚫음)
visited=[[[0]*(k+1) for _ in range(m)] for _ in range(n)]

print(bfs(n,m,k,0)) # 시작점은 벽뚫은적 없으므로, wallCnt=0
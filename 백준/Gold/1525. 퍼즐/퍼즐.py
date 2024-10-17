# https://www.acmicpc.net/problem/1525
# 퍼즐

"""
원래처럼 visited를 공유하는게 아님. 각 자식노드마다 그래프 모양이 다르므로.
즉, 퍼즐을 문자열로 생각하여 이 상태 그래프를 이용하여, 방문처리를 진행해야함.
그러면, 자식노드들의 그래프 모양이 다르므로 방문처리가 쉬워짐. (딕셔너리 활용)
"""

from collections import deque
input=__import__('sys').stdin.readline

def bfs(init):
    q=deque([init])
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    
    while q:
        status_puzzle=q.popleft()
        if status_puzzle=="123456780":
            return visited[status_puzzle]
        # 1차원의 빈칸 위치 -> 2차원의 행열 인덱스
        zero_idx_from_1=status_puzzle.index('0')
        x,y=zero_idx_from_1//3,zero_idx_from_1%3
        
        # 상하좌우 탐색 및 빈칸위치 스와핑
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<3 and 0<=ny<3:
                # 새로운 퍼즐 견적 맞추기
                new_status=list(status_puzzle)
                new_zero_idx_from_2=nx*3+ny # 새로운 위치의 빈칸위치 2차원->1차원 좌표
                new_status[zero_idx_from_1],new_status[new_zero_idx_from_2]=new_status[new_zero_idx_from_2],new_status[zero_idx_from_1]
                new_puzzle="".join(new_status)
                # 이 새로운 퍼즐이 방문딕셔너리에 없다면, 추가
                if new_puzzle not in visited:
                    visited[new_puzzle]=visited[status_puzzle]+1
                    q.append(new_puzzle)
                    
    return -1


init_puzzles=""
for _ in range(3):
    init_puzzles+="".join(map(str,[*map(int,input().split())]))

visited={init_puzzles:0} # 퍼즐모양:해당 퍼즐의 이동횟수
print(bfs(init_puzzles))
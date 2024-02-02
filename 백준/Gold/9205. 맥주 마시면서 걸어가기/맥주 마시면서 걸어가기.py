# Kastenlauf
# https://www.acmicpc.net/problem/9205
"""
맨허튼 거리를 몰라서, 그래프를 표현하는 방식에 대해 공부하는 좋은 계기가 되었다.
간단하게만 말하자면, 좌표계를 이용한 유클리드 방식과 달리
'좌표를 거리로 보는 방식'을 맨허튼 거리라고 부른다.

1. 최대,최소 거리를 묻는 문제가 아닌, '도달이 가능한가'에 대한 문제이다.
    => 어떠한 경로가 되었든, '편의점을 통해 목적지 도달이 가능한가'만을 체크하면 된다.
2. 맨허튼 그래프 방식은 좌표가 거리이다.
    => 맥주 한박스를 들고 이동가능한 최대 거리는 20병*50m=1000m이다.
3. 집->편의점1,...->목적지까지 어떤 경로든 가능한지 확인한다.
    => 집->편의점1, 집->편의점2 ...를 확인한다. (1)
    => 편의점1->편의점n 또는 편의점1->축제를 확인한다. (2)
    => 즉, 집 -> (편의점n -> 편의점 n)*n -> 목적지 이므로,
    => '자식노드들을 모두 방문하는 BFS 탐색 방식'
    => 탐색 노드 대상: 편의점, 간선 체크 방식: 현재 좌표(거리)에서 자식노드까지의 거리<=1000
"""
import sys
from collections import deque
input=sys.stdin.readline

def bfs(sx,sy):
    global goal_x,goal_y,conv_cnt
    q=deque([(sx,sy)]) # 시작 정점: 집
    
    while q:
        x,y=q.popleft() # 집 또는 편의점
        # 집~목적지 거리 <= 1000 또는 편의점~목적지 <= 1000
        if abs(x-goal_x)+abs(y-goal_y)<=1000:
            print("happy")
            return
        # 집->편의점(next node) 또는 편의점->편의점(next node) 가능한지 탐색.
        for i in range(conv_cnt):
            # 해당 편의점 방문하지 않았고
            # 해당 편의점까지의 거리가 1000미터 이하면
            if (conv_list[i][2]==0) and (abs(x-conv_list[i][0])+abs(y-conv_list[i][1])<=1000):
                q.append((conv_list[i][0],conv_list[i][1])) # 방문 가능
                conv_list[i][2]=1 # 방문 처리.
                
    print("sad")
    
for _ in range(int(input())):
    conv_cnt=int(input())
    home_x,home_y=map(int,input().split())
    conv_list=[] # 편의점 좌표 위치(bfs에서 거리로 치환해서 계산)
    for i in range(conv_cnt):
        # conv_list 원소 구조 : x좌표,y좌표,편의점[x][y] 방문했는가
        conv=[*map(int,input().split())] # 좌표 x,y
        conv.append(0) # visit 여부를 위한 새로운 원소
        conv_list.append(conv)
    goal_x,goal_y=map(int,input().split())
    
    bfs(home_x,home_y) # 집에서부터 탐색 시작.
    
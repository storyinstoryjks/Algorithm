"""
난이도: 보통
시간: 45분

드래곤 커브의 규칙을 찾는 것이 핵심이다.
1. k세대의 드래곤 커브 생성은 k-1세대 방향의 +1이다.
    => 2세대 드래곤 커브를 만든다고 가정하면
    => 2개의 선이 존재.(시작점~중간점, 중간점~끝점)
    => 중간점~끝점의 방향+1, 시작점~중간점의 방향+1
    => 이런식으로, 'k-1세대의 마지막 선분의 생성 방향+1'
2. k세대의 드래곤 커브 생성 규칙을 통해, 끝점에서부터 차례로 방향을 더해나가면 된다.
    => 시작점 -> 커브 생성 -> 끝점=이전 시작점 (갱신작업)
    => 이런식으로 하면, '이어서 선분 생성이 된다.'
3. 행렬을 편하게 보기 위해, y,x를 대칭으로 바꾼다. (y,x=x,y)
"""

# Dragon Curve

from sys import stdin 
input=stdin.readline

def get_path(d,g):
    curve=[d] # 시작점의 방향만 들어있는 초기 배열
    # g세대까지 방향 탐색(k세대)
    for _ in range(g):
        # k-1세대의 마지막 선분의 방향부터 탐색
        for i in range(len(curve)-1,-1,-1):
            # 현재 타겟 기준, 방향+1
            curve.append((curve[i]+1)%4)
    return curve
        
def curving(sy,sx,path):
    for D in path:
        sx+=dx[D] # 시작점 갱신
        sy+=dy[D] # 시작점 갱신
        if not(0<=sx<101 and 0<=sy<101):
            continue # 행렬 범위를 넘어가면 드래곤 커브로 취급 안함.
        arr[sx][sy]=1 # 선분 그리기 처리.

arr=[[0]*101 for _ in [0]*101]
dx,dy=[0,-1,0,1],[1,0,-1,0] # d값에 해당되는 방향.(0~4)

for _ in [0]*int(input()):
    y,x,d,g=map(int,input().split()) # matrix를 대칭으로 돌려서 생각.
    arr[x][y]=1 # 시작점 먼저 드래곤 커브 체크.
    curve=get_path(d,g) # 해당 g세대까지 만드는 방향 탐색.
    curving(y,x,curve) # 탐색된 방향을 토대로 순서대로 이어서 선분 그리기.

ans=0
for i in range(100):
    for j in range(100):
        # 사각형 위치 탐색
        if arr[i][j]==1 and arr[i+1][j]==1 and arr[i][j+1]==1 and arr[i+1][j+1]==1:
            ans+=1
print(ans)
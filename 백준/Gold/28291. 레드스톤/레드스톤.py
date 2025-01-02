# https://www.acmicpc.net/problem/28291
# 레드 스톤
# 구현,그래프탐색

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(root):
    q=deque([root])
    
    while q:
        x,y,power=q.popleft()
        if power<1: # 전기신호가 없는 경우 굳이 할 필요없음
            continue
        for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<w and 0<=ny<h:
                # 다음 회로블록이 램프 또는 가루인 경우
                # 그리고
                # 미방문 또는 (방문했지만, 기처리된 전기신호보다 현재 전기신호가 높은 경우)
                if board[nx][ny] in ['lamp','dust'] and visited[nx][ny]<power:
                    visited[nx][ny]=power
                    if board[nx][ny]!='lamp':
                        q.append((nx,ny,power-1))
                    
def check_lamps():
    while lamps:
        x,y=lamps.pop()
        if visited[x][y]==0:
            return False
    return True


w,h=map(int,input().split())
n=int(input())
board=[['' for _ in range(h)] for _ in range(w)]
visited=[[0]*h for _ in range(w)] # 전기신호 저장배열 및 방문처리
lamps,blocks=[],[]

for _ in range(n):
    label,x,y=input().split()
    x=int(x);y=int(y)
    if 'block' in label:
        blocks.append((x,y,15))
        board[x][y]='block'
    elif 'dust' in label:
        board[x][y]='dust'
    else:
        lamps.append((x,y))
        board[x][y]='lamp'

# 모든 레드스톤 블록들을 각 시작점으로 BFS
for start in blocks:
    bfs(start)

print(['failed','success'][check_lamps()])
            
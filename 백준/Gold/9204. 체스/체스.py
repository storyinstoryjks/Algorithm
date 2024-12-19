# https://www.acmicpc.net/problem/9204
# 체스
# 그래프 탐색, 구현

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

def bfs(si,sj,gi,gj):
    q=deque([(si,sj,[(si,sj)])]) # posX,posY,path(==visited)
    
    while q:
        x,y,path=q.popleft()
        for d in range(7,0,-1):
            for dx,dy in [(-d,-d),(d,-d),(-d,d),(d,d)]:
                nx,ny=x+dx,y+dy
                if 64<nx<73 and 0<ny<9:
                    if (nx,ny)==(gi,gj) and len(path)<5:
                        return f'{len(path)} ' + ' '.join(f'{chr(i)} {j}' for i,j in path)+f' {chr(gi)} {gj}'
                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny,path+[(nx,ny)]))
    
    return 'Impossible'
    
for _ in range(int(input())):
    sx,sy,gx,gy=input().split()
    visited=set()
    visited.add((ord(sx),sy))
    if (sx,sy)==(gx,gy):
        print(0,sx,sy)
    else:
        print(bfs(ord(sx),int(sy),ord(gx),int(gy)))


import sys
N, K = map(int, sys.stdin.readline().split())
pan = []
game = [[[] for j in range(N)] for i in range(N)]
def moved(moved_list, next_loc, loc): # 이동시키기
    while moved_list:
        moving_i = moved_list.pop()
        game[loc[0]][loc[1]].pop() # 원래 위치에서 제거
        game[next_loc[0]][next_loc[1]].append(moving_i) # 다음 위치로 이동
        horse[moving_i] = [next_loc[0], next_loc[1], horse[moving_i][2]] # 이동한 후 말들의 위치 업데이트
def ifblue(x, y, d, i): # 파란색이라면
    nx = x + direct[d][0]
    ny = y + direct[d][1]
    if nx < 0 or ny<0 or nx>=N or ny>=N or pan[nx][ny] == 2:
        # horse 업데이트 하고 가만히
        return
    else:
        on_i = game[x][y][game[x][y].index(i):]
        if pan[nx][ny] == 1:
            moved(on_i, [nx,ny], [x,y])
        else:
            on_i.reverse()
            moved(on_i, [nx,ny], [x,y])
            


for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    pan.append(line)
# 0은 흰색, 1은 빨간색, 2는 파란색
horse = []
for i in range(K):
    x, y, d = map(int, sys.stdin.readline().split())
    horse.append([x-1,y-1,d-1])
    game[x-1][y-1].append(i)
# d => 오왼위아래
answer = -1
direct = [[0,1], [0,-1], [-1,0], [1,0]]
index = 0
flag = False
while index <= 1000:
    index += 1
    # 구현
    # 말의 이동
    for i, val in enumerate(horse):
        x,y,d = val
        nx = x + direct[d][0]
        ny = y + direct[d][1]
        if nx < 0 or ny<0 or nx>=N or ny>=N or pan[nx][ny] == 2:
            if d%2==1:
                d -= 1
            else:
                d += 1
            horse[i] = [x, y, d]
            ifblue(x, y, d, i)
        else:
            # 말의 위에 위치한 말들을 찾고
            on_i = game[x][y][game[x][y].index(i):]
            
            if pan[nx][ny] == 1:
                moved(on_i, [nx,ny], [x,y])                
            else:
                on_i.reverse()
                moved(on_i, [nx,ny], [x,y])
    # 종료 조건
        for i in range(N):
            for j in range(N):
                if len(game[i][j]) >= 4:
                    answer = index
                    flag = True
                    break
    if flag == True:
        break
print(answer)
"""
난이도: 보통
시간: 50분

[요구사항 파악 핵심]
1. 토네이도 방향 전환의 규칙은?
2. 해방 방향의 거리 변화는?
3. 방향별 모래 비율 좌표의 변화는?

[알고리즘 설계]
<1. 토네이도 방향 전환의 규칙>
=> 문제에서 토네이도 방향을 잘 살펴보면 다음과 같은 규칙이 존재한다.
    방향그룹 : (왼쪽,아래,오른쪽,위), (왼쪽,아래,오른쪽,위), ... (반복)
=> 즉, 방향 전환은 dir=[왼쪽,아래,오른쪽,위] 배열의 인덱스로 접근하면 된다.

<2. 해당 방향의 거리 변화>
=> 1번과 함께 발견되는 규칙이다.
=> 중심 좌표를 기준으로 거리를 체크해보자.
    1번째 방향그룹 : (1,1,2,2)
    2번째 방향그룹 : (3,3,4,4)
    3번째 방향그룹 : (5,5,6,6)
    즉, '방향 전환이 2번 이루어졌을 때, 해당 방향의 거리가 +1이 된다.'

<3. 방향별 모래 비율 좌표 변화>
=> 90도로 회전했을 때의, 흩어지는 비율의 좌표가 달라진다.
=> 이에 따른 좌표 변화를 일반화하는 것이 핵심이다.
=> 두가지 방식이 존재한다.
    (1) 모래 좌표 비율만 담는 n*n 배열을 통해, A배열에 덧대어 확인하는 방식.
        => 일명, 딥러닝의 CNN 원리와 같다.
        => 모래 좌표 비율만 담는 n*n배열을 B배열이라 해보자.
        => A배열의 중심좌표와 B배열의 중심좌표 (기준: 문제 설명 기준 y)를 통일시켜 배열을 덧댄다.
        => 방향별로 90도 회전하는 것이므로, 'B배열을 90도마다 전치시키면 된다.'
        => 방향 위쪽 : 왼쪽 방향 기준 90도 회전. (1번째 전치)
        => 방향 오른쪽 : 방향 위쪽 기준 90도 회전. (2번째 전치) 이런식으로!
    (2) 회전했을 때의 모래 좌표 일반화 공식을 사용. (필자 선택)
        => 좌표평면계의 x/y축 대칭을 각각 이용하여, "왼쪽 방향의 모래 좌표 기준, 대칭 좌표들을 일반화!"
        => 왼쪽 방향의 모래 좌표를 (x,y)라 하자.
            아래쪽 : (-y,x)
            위쪽 : (y,-x)
            오른쪽 : (x,-y)
        => 그러므로, 현재 방향을 기준으로 '흩어지는 대상 모래(y) 좌표 + 비율 좌표'를 진행하면 된다.

나머지 세부적인 절차는 주석 설명.
"""

# 20057 : shark and tornado
# https://www.acmicpc.net/problem/20057

from sys import stdin
input=stdin.readline

def spread_sand(cx,cy):
    global ans,curDir,dirCnt,changeCnt
    
    curSand=0 # 비율에 따른 양 총합
    alpha=(cx+dx[curDir],cy+dy[curDir]) # 알파 좌표
    
    # 모래 비율 좌표들 모두 체크
    for ddx,ddy,per in percent_dir:
        ## 일반화 공식을 통해, 모래 비율 좌표 회전 처리.
        # Bottom
        if curDir==1:ddx,ddy=-ddy,ddx
        # Right
        elif curDir==2:ddx,ddy=ddx,-ddy
        # Top
        elif curDir==3:ddx,ddy=ddy,-ddx
        
        ## 현재 흩어지는 모래 좌표 Y 기준, 모래 비율 자리 찾기.
        x,y=cx+ddx,cy+ddy
        
        sp_sand=(board[cx][cy]*per)//100 # 비율에 따른 모래양
        # 범위 내라면, 그 자리에 모래 더하기
        if 0<=x<n and 0<=y<n:board[x][y]+=sp_sand
        else:ans+=sp_sand # 범위 외, 격자 밖!
        curSand+=sp_sand # 총합 갱신
    
    left_sand=board[cx][cy]-curSand # 나머지 모래=원래모래양-총합
    board[cx][cy]=0 # Y는 다 흩어졌으므로 0
    # 알파 자리 범위 체크
    if 0<=alpha[0]<n and 0<=alpha[1]<n:
        board[alpha[0]][alpha[1]]+=left_sand
    else: # 알파 자리가 범위를 넘어가면, 격자 밖!
        ans+=left_sand
    
n=int(input())
board=[[*map(int,input().split())] for _ in range(n)]
dx=[0,1,0,-1] # left, bottom, right, top
dy=[-1,0,1,0]
# 답, 현재좌표,현재좌표,현재방향,해당방향거리,방향전환개수(2의배수)
ans,curX,curY,curDir,dirCnt,changeCnt=0,n//2,n//2,0,1,1

percent_dir=[(-1,1,1),(1,1,1),(-1,0,7),
             (1,0,7),(-1,-1,10),(1,-1,10),
             (-2,0,2),(2,0,2),(0,-2,5)] # (dx,dy,percentage)

# 토네이도 좌표가 (0,0)이 될때까지 반복
while (curX,curY)!=(0,0):
    # Move Tornado
    for _ in range(dirCnt): # 현재 방향 기준, 거리만큼 토네이도 이동
        curX+=dx[curDir] # 흩어지는 모래 Y의 x좌표
        curY+=dy[curDir] # 얘는 y좌표
        # 흩어지는 모래 Y의 양이 0이면 흩어지는게 없으므로, move 생략
        if board[curX][curY]>0:
            spread_sand(curX,curY)

    # Change Direction
    curDir=(curDir+1)%4
    
    # Change Distance & DistanceCnt
    if changeCnt==2:
        changeCnt=1
        if dirCnt!=n-1:dirCnt+=1
    else:changeCnt+=1
    
print(ans)
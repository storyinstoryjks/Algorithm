# https://www.acmicpc.net/problem/9184
# 신나는 함수 실행
# 재귀,DP

# Bottom-Up 하향식
input=__import__('sys').stdin.readline

while True:
    a,b,c=map(int,input().split())
    if (a,b,c)==(-1,-1,-1):
        break
    
    dp=[[[0]*21 for _ in range(21)] for _ in range(21)]

    # 초기 조건 채우기
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i==0 or j==0 or k==0:
                    dp[i][j][k]=1
    
    # 1~20까지 DP테이블 채우기
    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                if i<j<k:
                    dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
                else:
                    dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]
    
    # 답 출력
    answer=0
    if a<=0 or b<=0 or c<=0:
        answer=1
    elif a>20 or b>20 or c>20:
        answer=dp[20][20][20]
    else:
        answer=dp[a][b][c]
    print(f"w({a}, {b}, {c}) = {answer}")
# https://www.acmicpc.net/problem/2110
# 공유기 설치
# 이분 탐색

"""
난이도 : 쉬움~보통
시간 : 30분

공유기 간 거리를 이진탐색으로 찾는 것이 핵심.
- 현재 거리보다 더 공유기가 설치된다면, 거리를 늘리자.
- 적다면, 거리를 줄이자.
"""

from sys import stdin
input=stdin.readline

n,c=map(int,input().split())
homes=sorted([int(input()) for _ in range(n)])

## 공유기 거리 탐색을 위한 자료
start=1 # 최소거리(1)
end=homes[-1]-homes[0] # 최대거리(각 끝 집좌표의 차)
history=0 # 정답

while start<=end:
    mid=(start+end)//2 # 현재 탐색 공유기 거리
    
    ## 공유기 설치 가능 체크
    cnt=1 # 첫번째 집에 미리 설치
    cur=homes[0] # 설치된 전집
    for i in range(1,n):
        if mid+cur<=homes[i]: # 다음집거리 >= 전집거리+공유기거리
            cnt+=1
            cur=homes[i]
    
    ## 설치한 공유기 수 >= 목표수
    if cnt>=c:
        start=mid+1 # 더 크게 늘려보기
        history=mid # 공유기 설치가 가능한것이므로 중간 저장
    else:
        end=mid-1 # 목표수만큼 못 설치하므로, 거리를 줄이기

print(history)
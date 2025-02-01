# https://www.acmicpc.net/problem/13904
# 과제
# 우선순위큐, 정렬, 그리디

from sys import stdin 
import heapq
input=stdin.readline

n=int(input())
max_heap=[]
max_deadline,answer=0,0 # 몇일날부터 스케줄을 짤 것인가

for _ in range(n):
    d,w=map(int,input().split())
    heapq.heappush(max_heap,(-w,d))
    max_deadline=max(max_deadline,d)

schedule=[False]*(max_deadline+1) # 스케줄 할당표
                                  # True : 해당 인덱스 날짜에 과제 활동 배정되있음.

# 높은 점수부터 스케줄 할당 시작
while max_heap:
    w,d=heapq.heappop(max_heap)
    
    # 해당 과제의 d일부터 마감일 1일전까지 배정 가능한지 체크
    for day in range(d,0,-1):
        if schedule[day]: # 이미 배정된 과제가 있음.
            continue
        # 해당 day에 배정 가능하면
        schedule[day]=True
        answer+=(-w)
        break

print(answer)
# https://www.acmicpc.net/problem/28107
# 회전초밥
# 큐,우선순위 큐

input=__import__('sys').stdin.readline
deque=__import__('collections').deque
import heapq

n,m=map(int,input().split())
order_lists=[[] for _ in range(200001)]

for id in range(n):
    for order in [*map(int,input().split())][1:]:
        heapq.heappush(order_lists[order],id+1)

answer=[0]*(n+1)
for cur_sushi in [*map(int,input().split())]:
    try:
        cur_id=heapq.heappop(order_lists[cur_sushi])
        answer[cur_id]+=1
    except:
        continue
    
print(*answer[1:])
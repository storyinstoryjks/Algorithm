import heapq

def solution(info, n, m):
    # b를 최대한 많이 먹으면서, 큰 a를 제거하는 방향
    answer,min_heap = 0,[]
    prioritys={(3, 1): 0, (2, 1): 1, (3, 2): 2, (3, 3): 3, (2, 2): 4, (1, 1): 5, (2, 3): 6, (1, 2): 7, (1, 3): 8}
    
    for a,b in info:
        heapq.heappush(min_heap,(prioritys[(a,b)],a,b))
    
    cur_m=0
    while min_heap:
        p,a,b=heapq.heappop(min_heap)
        t=cur_m+b
        if t<m:
            cur_m=t
            continue
        answer+=abs(a)
        
    return answer if answer<n else -1
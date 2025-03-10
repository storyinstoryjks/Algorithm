import heapq

def solution(players, m, k):
    cur_server,add_server_cnt=0,0
    server_dashboard=[]
    
    for start_time in range(len(players)):
        user_cnt,end_time=players[start_time],start_time+1
        if user_cnt<m:
            if server_dashboard:
                end,cnt=heapq.heappop(server_dashboard)
                if end==end_time:
                    cur_server-=cnt
                else:
                    heapq.heappush(server_dashboard,(end,cnt))
            continue
            
        need_server_cnt=user_cnt//m
        if need_server_cnt>cur_server:
            open_cnt=need_server_cnt-cur_server
            heapq.heappush(server_dashboard,(start_time+k,open_cnt)) # (현재 개설된 서버 종료시간, 개설된 서버 개수)
            cur_server+=open_cnt
            add_server_cnt+=open_cnt
        
        if server_dashboard:
            end,cnt=heapq.heappop(server_dashboard)
            if end==end_time:
                cur_server-=cnt
            else:
                heapq.heappush(server_dashboard,(end,cnt))
    
    return add_server_cnt

# 1 -> 3~6
# 2 -> 6~9
# 3 -> 9~12
# m으로 나눈 몫
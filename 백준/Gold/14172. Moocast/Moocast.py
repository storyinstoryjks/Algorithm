# https://www.acmicpc.net/problem/14172
# Moocast
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline
cal_distance=lambda X,Y:X**2+Y**2 # X=abs(x1-x2), Y=abs(y1-y2)

def bfs(flag_node_idx):
    q=deque([flag_node_idx])
    visited=[False for _ in range(n)]
    visited[flag_node_idx]=1
    
    cnt=1
    while q:
        cur_node_idx=q.popleft()
        for target_node_idx in range(n):
            if possible_distances[cur_node_idx][target_node_idx] and not visited[target_node_idx]:
                visited[target_node_idx]=True
                q.append(target_node_idx)
                cnt+=1
    return cnt


n=int(input())
adj_list=[tuple(map(int,input().split())) for _ in range(n)]
possible_distances=[[False]*n for _ in range(n)]

# 모든 노드에 대한 각 노드 거리 도달 여부
for cur_node_idx in range(n):
    for target_node_idx in range(n):
        if cur_node_idx==target_node_idx:
            possible_distances[cur_node_idx][target_node_idx]=True
            continue
        
        x1,y1=adj_list[cur_node_idx][0],adj_list[cur_node_idx][1]
        x2,y2=adj_list[target_node_idx][0],adj_list[target_node_idx][1]
        
        # 피타고라스 c제곱을 이용한 거리 계산
        if adj_list[cur_node_idx][2]**2 >= cal_distance(abs(x1-x2),abs(y1-y2)):
            possible_distances[cur_node_idx][target_node_idx]=True

# 모든 노드를 시작점으로 BFS
answer=-1
for node_idx in range(n):
    answer=max(answer,bfs(node_idx))

print(answer)
# https://www.acmicpc.net/problem/13463
# Brexit
# 그래프 탐색, bfs

input=__import__('sys').stdin.readline
deque=__import__('collections').deque

def bfs(root):
    q=deque([root])
    leave_node_flags[root]=True
    
    while q:
        cur_node=q.popleft()
        # 탈퇴한 cur_node 국가의 파트너 국가들 탐색
        for next_node in graph[cur_node]:
            delete_edges_counts[next_node]+=1 # 해당 파트나 국가 간선 제거 가정.
            # 현재 Y의 간선개수 >= 초기 간선개수//2를 양변에 2를 곱한 수식으로 변형.
            # 나눌때 홀수인 경우, +1을 해야하기 때문에, 코드를 줄이기 위해서!
            # 초기 파트너 연합수(간선수) 절반 이상이고, 탈퇴하지 않았다면
            if delete_edges_counts[next_node]*2>=init_nodes_edges_counts[next_node] and not leave_node_flags[next_node]:
                leave_node_flags[next_node]=True # 해당 파트너 국가 탈퇴 처리
                q.append(next_node)

C,P,X,L=map(int,input().split())
graph=[[] for _ in range(C+1)]
delete_edges_counts=[0]*(C+1) # 탐색 시, 해당 노드의 제거되는 간선 개수
init_nodes_edges_counts=[0]*(C+1) # 초기 해당 노드에 연결된 간선 개수

for _ in range(P):
    start,end=map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

# init_nodes_edges_counts=[0]+[len(i) for i in graph]
for i in range(1,C+1):
    init_nodes_edges_counts[i]=len(graph[i])

leave_node_flags=[False]*(C+1) # 해당 노드가 연합 탈퇴를 했는지 여부
bfs(L) # 첫 탈퇴 국가를 시작으로 그래프 탐색 시작.

print(['stay','leave'][leave_node_flags[X]])
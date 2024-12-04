# https://www.acmicpc.net/problem/10472
# 십자뒤집기
# 그래프 탐색, 브루트포스

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

d=[
    [0,1,3],[0,1,2,4],[1,2,5],
    [0,3,4,6],[1,3,4,5,7],[2,4,5,8],
    [3,6,7],[4,6,7,8],[5,7,8]
] # 각 지점을 클릭했을 시, 1차원 배열상에서 변하는 위치점.

def bfs(start_status):
    q=deque([(0,start_status)]) # graph_depth,status
    visited=set()
    visited.add(start_status)
    
    while q:
        depth,status=q.popleft()
        # 모든 경우 탐색
        for next_click in range(9):
            next_status=[*status]
            # 각 경우에서 색깔 변하기 처리
            for change_place in d[next_click]:
                if next_status[change_place]=='0':
                    next_status[change_place]='1'
                else:
                    next_status[change_place]='0'
            next_status=''.join(next_status)
            # 정답이면
            if next_status==target:
                return depth+1
            # 다음 상태가 새로운 상태라면
            if next_status not in visited:
                q.append((depth+1,next_status))
                visited.add(next_status)
    
    
for _ in range(int(input())):
    target=""
    init_status='0'*9
    
    for i in range(3):
        for e in [*input()]:
            if e=='*':
                target+='1'
            elif e=='.':
                target+='0'
    
    print(0 if target==init_status else bfs(init_status))
# https://www.acmicpc.net/problem/18112
# 이진수 게임
# 그래프 탐색

deque=__import__('collections').deque
input=__import__('sys').stdin.readline

start=input().strip()
end=input().strip()
dec_end=int(end,2)

q=deque([(start,0)])
visited=set()
visited.add(int(start,2))

while q:
    bin_x,cnt=q.popleft()
    dec_x=int(bin_x,2)
    if dec_x==dec_end:
        print(cnt)
        break
    # 1번째 동작
    for i in range(len(bin_x)-1):
        dec_nx=dec_x^(1<<i)
        if dec_nx not in visited:
            visited.add(dec_nx)
            q.append((bin(dec_nx)[2:],cnt+1))
    # 2번째 동작
    if dec_x+1 not in visited:
        visited.add(dec_x+1)
        q.append((bin(dec_x+1)[2:],cnt+1))
    # 3번째 동작
    if dec_x!=0 and dec_x-1 not in visited:
        visited.add(dec_x-1)
        q.append((bin(dec_x-1)[2:],cnt+1))
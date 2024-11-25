import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    di = [1, -1, K]
    while q:
        idx, dir, t = q.popleft()
        for d in range(3):
            next_idx = idx + di[d]
            if next_idx >= N: return True
            if next_idx <= t: continue

            if arr[dir][next_idx] == 1 and d != 2 and visited[dir][next_idx] == False:
                q.append((next_idx, dir, t+1))
                visited[dir][next_idx] = True

            elif d == 2 and arr[1-dir][next_idx] == 1 and visited[1-dir][next_idx] == False:
                q.append((next_idx, 1-dir, t+1))
                visited[1-dir][next_idx] = True

    return False


N, K = map(int, input().split())
left = list(map(int, input().strip()))
right = list(map(int, input().strip()))
visited = [[False for _ in range(N)] for _ in range(2)]
arr = [left, right]
visited[0][0] = True

print(1 if bfs() == True else 0)
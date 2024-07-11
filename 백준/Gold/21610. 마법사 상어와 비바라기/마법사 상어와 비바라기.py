import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

rx = [0, -1, -1, -1, 0, 1, 1, 1]
ry = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for direction in directions:
    d, m = direction[0] - 1, direction[1] % N
    not_cloud = set()
    while clouds:
        x, y = clouds.pop()
        nx, ny = (x + m*rx[d]) % N, (y + m*ry[d]) % N
        graph[nx][ny] += 1
        not_cloud.add((nx, ny))

    for nx, ny in not_cloud:
        count = 0
        for _ in range(1, 8, 2):
            nnx = nx + rx[_]
            nny = ny + ry[_]
            if 0 <= nnx < N and 0 <= nny < N:
                if graph[nnx][nny]:
                    count += 1
        graph[nx][ny] += count

    for x in range(N):
        for y in range(N):
            if (x, y) not in not_cloud:
                if graph[x][y] >= 2:
                    clouds.append((x, y))
                    graph[x][y] -= 2

print(sum([sum(_) for _ in graph]))
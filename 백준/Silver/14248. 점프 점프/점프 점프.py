# https://www.acmicpc.net/problem/14248
# 점프 점프
# 그래프 탐색

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    left_child=x-A[x]
    right_child=x+A[x]
    if 0<=left_child<n and not visited[left_child]:
        visited[left_child]=1
        dfs(left_child)
    if 0<=right_child<n and not visited[right_child]:
        visited[right_child]=1
        dfs(right_child)

n=int(input())
A=[*map(int,input().split())]
root=int(input())
root-=1

visited=[0]*n
visited[root]=1
dfs(root)
print(sum(visited))
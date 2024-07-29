# https://www.acmicpc.net/problem/2805
# 나무 자르기
# 이분 탐색

n,m=map(int,input().split())
trees=[*map(int,input().split())]
start,end=0,max(trees) # 절단기 설정범위: 0~나무최대길이
height=0

# 이분 탐색
while start<=end:
    mid=(start+end)//2 # 절단기 중간높이
    left_trees=0 # 자른 후 남은 나무 길이 총합
    for tree in trees:
        if tree>=mid:
            left_trees+=tree-mid
    # 남은 나무 길이 총합 >= 목표치
    if left_trees>=m:
        height=max(height,mid)
        start=mid+1 # 이보다 더 높은 절단기 높이 가능한지 체크
    else:
        end=mid-1 # 목표치에 도달하는 절단기 높이 찾기

print(height)
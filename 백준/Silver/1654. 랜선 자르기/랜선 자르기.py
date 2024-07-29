# https://www.acmicpc.net/problem/1654
# 랜선 자르기
# 이분 탐색

k,n=map(int,input().split())
lines=[int(input()) for _ in range(k)]
start,end=0,2147483647 # 랜선의 길이 범위: 0~최대길이
weight=0 # 정답(최대 랜선 길이)

while start<=end:
    mid=(start+end)//2 # 자를 길이
    cnt=0 # 자른 랜선의 개수
    for line in lines:
        if line>=mid:
            cnt+=line//mid
    # n개 이상 나올시
    if cnt>=n:
        weight=max(weight,mid)
        start=mid+1 # 이보다 더 긴 랜선 길이로 자를 수 있는지 체크
    else:
        end=mid-1 # 목표치 개수 n이 나오도록 mid값 낮추기
                  # 너무 길게 잘랐기에, n개보다 덜 나온것.

print(weight)
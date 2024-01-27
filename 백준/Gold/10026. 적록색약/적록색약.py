# 10026 : ColorBlind
import sys
input=sys.stdin.readline

def dfs1(x,y):
    stk=[[x,y]]
    while stk:
        #print(stk)
        e=stk.pop(0)
        x,y=e
        visitedColor1[x][y]=1
        #left
        if y-1>=0 and not visitedColor1[x][y-1] and [x,y-1] not in stk and graph[x][y-1]==graph[x][y]:
            stk=[[x,y-1]]+stk
        #right
        if y+1<n and not visitedColor1[x][y+1] and [x,y+1] not in stk and graph[x][y+1]==graph[x][y]:
            stk=[[x,y+1]]+stk
        #top
        if x-1>=0 and not visitedColor1[x-1][y] and [x-1,y] not in stk and graph[x-1][y]==graph[x][y]:
            stk=[[x-1,y]]+stk
        #bottum
        if x+1<n and not visitedColor1[x+1][y] and [x+1,y] not in stk and graph[x+1][y]==graph[x][y]:
            stk=[[x+1,y]]+stk

def dfs2(x,y):
    stk=[[x,y]]
    while stk:
        #print(stk)
        e=stk.pop(0)
        x,y=e
        visitedColor2[x][y]=1
        #left
        if y-1>=0 and not visitedColor2[x][y-1] and [x,y-1] not in stk and (graph[x][y-1]==graph[x][y] or (graph[x][y]=='R' and graph[x][y-1]=='G')
                                                                            or (graph[x][y]=='G' and graph[x][y-1]=='R')):
            stk=[[x,y-1]]+stk
        #right
        if y+1<n and not visitedColor2[x][y+1] and [x,y+1] not in stk and (graph[x][y+1]==graph[x][y] or (graph[x][y]=='R' and graph[x][y+1]=='G')
                                                                            or (graph[x][y]=='G' and graph[x][y+1]=='R')):
            stk=[[x,y+1]]+stk
        #top
        if x-1>=0 and not visitedColor2[x-1][y] and [x-1,y] not in stk and (graph[x-1][y]==graph[x][y] or (graph[x][y]=='R' and graph[x-1][y]=='G')
                                                                            or (graph[x][y]=='G' and graph[x-1][y]=='R')):
            stk=[[x-1,y]]+stk
        #bottum
        if x+1<n and not visitedColor2[x+1][y] and [x+1,y] not in stk and (graph[x+1][y]==graph[x][y] or (graph[x][y]=='R' and graph[x+1][y]=='G')
                                                                            or (graph[x][y]=='G' and graph[x+1][y]=='R')):
            stk=[[x+1,y]]+stk

n=int(input())
graph=[input() for _ in range(n)]
visitedColor1=[[0]*n for _ in range(n)]
visitedColor2=[[0]*n for _ in range(n)]
cnt1,cnt2=0,0

for i in range(n):
    for j in range(n):
        if not visitedColor1[i][j]:
            #print(f"#DFS({i},{j})")
            dfs1(i,j) # Normal Person
            cnt1+=1
        if not visitedColor2[i][j]:
            dfs2(i,j) # ColorBlind-Person
            cnt2+=1

print(cnt1,cnt2)
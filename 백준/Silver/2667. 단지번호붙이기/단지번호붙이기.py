# 2667 : Numbering Villige

def dfs(x,y):
    cnt=1
    stk=[[x,y]]
     
    while stk!=[]:
        #print(stk)
        e=stk.pop(0)
        x,y=e
        visited[x][y]=1
        # left
        if y-1>=0 and not visited[x][y-1] and [x,y-1] not in stk and home[x][y-1]=='1':
            stk=[[x,y-1]]+stk
            cnt+=1
        # right
        if y+1<n and not visited[x][y+1] and [x,y+1] not in stk and home[x][y+1]=='1':
            stk=[[x,y+1]]+stk
            cnt+=1
        # top
        if x-1>=0 and not visited[x-1][y] and [x-1,y] not in stk and home[x-1][y]=='1' :
            stk=[[x-1,y]]+stk
            cnt+=1
        # bottom
        if x+1<n and not visited[x+1][y] and [x+1,y] not in stk and home[x+1][y]=='1' :
            stk=[[x+1,y]]+stk
            cnt+=1
    
    return cnt

n=int(input())
home=[input()for _ in range(n)]
visited=[[0]*n for _ in range(n)]
ans=[]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and home[i][j]=='1':
            #print(f"#DFS:[{i},{j}]")
            ans.append(dfs(i,j))

ans.sort()
print(len(ans))
print('\n'.join(map(str,ans)))
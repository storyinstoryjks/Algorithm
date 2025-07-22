# https://www.acmicpc.net/problem/3758
# KCPC

for _ in range(int(input())):
    n,k,t,m=map(int,input().split())
    dash={}
    
    # dictionary init
    for i in range(1,n+1):
        dash[i]={
            'cnt':0,
            'apply':[0 for _ in range(k+1)],
            'apply_time':-1
        }
    
    # setting dashboard
    for time in range(m):
        team,no,score=map(int,input().split())
        dash[team]['cnt']+=1
        dash[team]['apply'][no]=max(dash[team]['apply'][no],score)
        dash[team]['apply_time']=max(dash[team]['apply_time'],time)
    
    # cal rank
    rank=sorted([(team,sum(dash[team]['apply'])) for team in range(1,n+1)],key=lambda x:(-x[1],dash[x[0]]['cnt'],dash[x[0]]['apply_time']))

    for i in range(n+1):
        if rank[i][0]==t:
            print(i+1)
            break
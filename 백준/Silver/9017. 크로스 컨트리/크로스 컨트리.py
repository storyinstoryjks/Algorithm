for _ in range(int(input())):
    n=int(input())
    states=[*map(int,input().split())]
    excludes=set(team for team in set(states) if states.count(team)<6)
    dashboard={}
    
    score=1
    for team in states:
        if team in excludes:
            continue
        try:
            dashboard[team].append(score)
        except:
            dashboard[team]=[score]
        score+=1
    
    min_team,min_score=[],-1
    for team in dashboard.keys():
        team_score=sum(dashboard[team][:4])
        if min_score==-1:
            min_team.append(team)
            min_score=team_score
            continue
        if team_score<min_score:
            min_team=[team]
            min_score=team_score
        elif team_score==min_score:
            min_team.append(team)
    
    if len(min_team)==1:
        print(min_team[0])
        continue

    print(min([(team,dashboard[team][4]) for team in min_team],key=lambda x:x[1])[0])
    
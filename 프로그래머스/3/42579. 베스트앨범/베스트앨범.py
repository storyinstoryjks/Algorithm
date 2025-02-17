def solution(genres, plays):
    answer = []
    
    play_genres={}
    play_songs={}
    
    for id in range(len(genres)):
        name=genres[id]
        try:
            play_genres[name]+=plays[id]
        except:
            play_genres[name]=plays[id]
        try:
            play_songs[name].append((id,plays[id]))
        except:
            play_songs[name]=[(id,plays[id])]
    
    for name in sorted(play_genres.keys(), key=lambda x:play_genres[x])[::-1]:
        t=sorted(play_songs[name], key=lambda x:(-x[1],x[0]))
        if len(t)<=1:
            answer.append(t[0][0])
        else:
            answer.append(t[0][0])
            answer.append(t[1][0])
    return answer
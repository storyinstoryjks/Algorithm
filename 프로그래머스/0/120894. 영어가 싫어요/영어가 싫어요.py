def solution(numbers):
    d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,
      'six':6,'seven':7,'eight':8,'nine':9}
    answer=""
    tmp=""
    for i in numbers:
        if len(tmp)<3:
            tmp+=i
        elif len(tmp)==3:
            if tmp in ['one','two','six']:
                answer+=str(d[tmp])
                tmp=""
            tmp+=i
        elif len(tmp)==4:
            if tmp in ['zero','four','five','nine']:
                answer+=str(d[tmp])
                tmp=""
            tmp+=i
        else:
            answer+=str(d[tmp])
            tmp=""
            tmp+=i
    answer+=str(d[tmp])
    return int(answer)
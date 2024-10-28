def solution(polynomial):
    tmp,answer=[0,0],''
    
    for i in polynomial.split(' + '):
        idx=i.find('x')
        if idx==-1:
            tmp[1]+=int(i)
        else:
            tmp[0]+=int(i[:idx] if i[:idx]!='' else '1')
            
    if tmp[0]>0:
        if tmp[0]>1:
            answer+=f"{tmp[0]}x"
        else:
            answer+="x"
    if tmp[1]>0:
        if answer=='':
            answer+=str(tmp[1])
        else:
            answer+=f" + {tmp[1]}"
    
    return answer
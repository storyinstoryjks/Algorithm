def candidate(area):
    arr=[]
    for i in range(3,int(area**.5)+1):
        if area%i==0:
            arr.append([area//i,i])
    return arr

def solution(brown, yellow):
    for width,height in candidate(brown+yellow):
        if (width-2)*(height-2)==yellow:
            return [width,height]
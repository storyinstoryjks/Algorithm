import heapq
n=int(input())
l=[int(input())for _ in[0]*n]
c=0
h=[]
if n<1:print(0)
else:
    for i in l[1:]:
        heapq.heappush(h,(-i,i))
    while h:
        if h[0][1]<l[0] and h.count(l[0])<2:
            break
        e=heapq.heappop(h)[1]-1
        heapq.heappush(h,(-e,e))
        l[0]+=1;c+=1
    print(c)
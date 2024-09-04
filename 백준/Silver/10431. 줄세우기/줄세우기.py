for k in range(int(input())):
    a=0
    l=[*map(int,input().split())][1:]
    for i in range(1,20):
        f,c=0,0
        for j in range(i-1,-1,-1):
            if l[j]>l[i]:
                if f==0:
                    c=j;f=1
                elif l[c]>l[j]:
                    c=j
        if f:
            a+=i-c
            for j in range(i,c,-1):
                l[j],l[j-1]=l[j-1],l[j]
        #print(l)
    print(k+1,a)
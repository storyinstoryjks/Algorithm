s=input();b=[*input()];l=len(b);r=[]
for i in s:
 r+=[i]
 if r[-l:]==b:r[-l:]=[]
print(''.join(r)or"FRULA")
'''
Four steps to finished this function:
1.initial: j is the tail of the profix list; i is the tail suffix list; the next list
2. if not math;
3. if math;

'''

def getNext(s:str):
    j=0
    next=[0]
    for i in range(1,len(s)):
        while j>0 and s[i]!=s[j]:
            j=next[j-1]
        if s[i]==s[j]:
            j+=1
        next.append(j)
    return next


next=getNext(s='aabaaf')
for i in next:
    print(i,end=' ')

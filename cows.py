def isValid(n,k,stalls,mid):
    prcow=stalls[0]
    count=1
    for i in stalls:
        if (i-prcow)>=mid:
            count+=1
            prcow=i
    return True if k==count else False
def solve(n,k,stalls):
    stalls.sort()
    si=0
    li=stalls[-1]-stalls[0]
    res=0
    while si<=li:
        mid=(si+li)//2
        if isValid(n,k,stalls,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
    return res
n=int(input())
k=int(input())
stalls=list(map(int,input().split()))
print(solve(n,k,stalls))
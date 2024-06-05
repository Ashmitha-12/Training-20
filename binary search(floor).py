def bs(l,si,li,se):
    floor=-1
    mid=(si+li)//2
    if si<=li:
        if l[mid]==se:
            return mid
        if l[mid]<se:
            floor=l[mid]
            return bs(l,mid+1,li,se)
        return bs(l,si,mid-1,se)
    return "return the things whatever u have"
l=list(map(int,input().split()))
se=int(input())
res=bs(l,0,len(l)-1,se)
print(res)
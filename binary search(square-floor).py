def square(n,si,li,floor):
    #1floor=-1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==n:
            floor=mid
            return mid
        if sq<n:
            floor=mid
            return square(n,mid+1,li,floor)
        return square(n,si,mid-1,floor)
    return floor
n=int(input())
si=0
li=n//2
floor=-1
print(square(n,si,li,floor))
def find(l,target_sum):
    i=0
    j=0
    current_sum=l[0]
    while j<len(l)-1:
        if current_sum==target_sum:
            print(l[i],l[j],current_sum)
            break
        elif current_sum>target_sum:
            current_sum-=l[i]
            i+=1
        else:
            j+=1
            current_sum+=l[j]
l=list(map(int,input().split(',')))
target_sum=int(input())
find(l,target_sum)


'''Finding triplet using two pointer'''
def find_triplets(arr,target_sum):
    i=0
    left=i+1
    right=len(arr)-1
    for i in range(len(arr)):
        while left<right:
            current_sum=arr[i]+arr[left]+arr[right]
            if current_sum==target_sum:
                return arr[i],arr[left],arr[right]
            elif current_sum<target_sum:
                left=left+1
            else:
                right=right-1
l=list(map(int,input().split()))
target_sum=int(input())
arr=sorted(l)
print(find_triplets(arr,target_sum))
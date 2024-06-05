def find(arr,target_sum):
    left=0
    right=len(arr)-1
    for i in range(len(arr)):
        while left<right:
            current_sum=arr[left]+arr[right]
            if current_sum==target_sum:
                return arr[left],arr[right]
            elif current_sum<target_sum:
                left=left+1
            else:
                right=right-1
l=[5,8,1,2,3]
target_sum=9
arr=sorted(l)
print(find(arr,target_sum))

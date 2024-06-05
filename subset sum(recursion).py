def isSubsetSum(arr, n, target_sum):
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target_sum]
target_sum = int(input("Enter the target sum: "))
arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
n = len(arr)
if isSubsetSum(arr, n, target_sum):
    print("True")
else:
    print("False")

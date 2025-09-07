#  Question Link : https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# brute force solution 
def maximum_sum_subarray_size_k(arr, k):
    n = len(arr)
    currSum = 0
    maxSum = float('-inf')
    for i in range(0, n - k+1):
        currSum += arr[i]
        for j in range(i + 1, i + k):
            currSum += arr[j]
        
        maxSum = max(maxSum, currSum)
        currSum = 0
    return maxSum if maxSum != float('-inf') else -1
    
# Optimize Solution 
def maximum_sum_subarray_size_k(arr, k):
    n = len(arr)
    currSum = 0
    maxSum = float('-inf')
    i = 0

    for j in range(n):
        currSum += arr[j]  # add next element

        # once window size is k, update maxSum and slide the window
        if j - i + 1 == k:
            maxSum = max(maxSum, currSum)
            currSum -= arr[i]  # remove element going out of the window
            i += 1

    return maxSum if maxSum != float('-inf') else -1    


print(maximum_sum_subarray_size_k([100, 200, 300, 400, 0], 2))

#  Question Link : https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
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
# https://leetcode.com/problems/maximum-average-subarray-i/
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currAvg = 0
        currSum = 0
        maxAvg = float('-inf')
        i = 0
        n = len(nums)

        for j in range(n):
            currSum += nums[j]

            if j - i + 1 == k:
                currAvg = currSum / k
                maxAvg = max(maxAvg, currAvg)
                currSum -= nums[i]
                i += 1
        return maxAvg if maxAvg != float('-inf') else -1
        
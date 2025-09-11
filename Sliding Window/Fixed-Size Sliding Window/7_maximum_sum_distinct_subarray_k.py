# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        i = 0
        maxSum = 0
        currSum = 0
        temp = []
        tempSet = set()
        for j in range(n):
            currSum += nums[j]
            temp.append(nums[j])
            if j - i + 1 == k:
                tempSet = set(temp)
                if k == len(tempSet):
                    maxSum = max(maxSum, currSum)
                currSum -= temp[0]
                temp = temp[1:]
                tempSet = set()
                i += 1
        return maxSum
                

sol = Solution()
print(sol.maximumSubarraySum([1,1,1,7,8,9], 3))
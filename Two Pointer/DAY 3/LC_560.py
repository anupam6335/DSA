# Subarray Sum Equals K — #560
#  problem link : https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pre_sum = []
        temp = 0
        for n in nums:
            temp += n 
            pre_sum.append(temp)
        print(pre_sum)

sol = Solution()

print(sol.subarraySum([1,1,1, 10, 24], 2))
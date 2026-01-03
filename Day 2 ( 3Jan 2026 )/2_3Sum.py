# problem Link : https://leetcode.com/problems/3sum/description/

from typing import List

class Solution:
    def twoSumHelper(self, k,  nums: List[int], res: List[List[int]]) -> None:
        i = k + 1
        j = len(nums) - 1

        while i < j:
            curr_sum = nums[i] + nums[k] + nums[j]
            if curr_sum < 0:
                i += 1
            elif curr_sum > 0:
                j -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                i += 1
                j -= 1

                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for k in range(0, n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            self.twoSumHelper(k, nums, res)
        return res


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
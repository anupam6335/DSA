# problem Link : https://leetcode.com/problems/4sum/description/


from typing import List 
class Solution:
    def twoSumHelper(self, k,l, target,  nums: List[int], res: List[List[int]]) -> None:
        i = l + 1
        j = len(nums) - 1

        while i < j:
            curr_sum = nums[i] + nums[k] + nums[j] + nums[l]
            if curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1
            else:
                res.append([nums[i], nums[j], nums[k], nums[l]])
                i += 1
                j -= 1

                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for k in range(0, n - 3):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            for l in range(k + 1, n- 2):
                if l > k + 1 and nums[l] == nums[l - 1]:
                    continue 
                self.twoSumHelper(k, l, target, nums, res)
        return res
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))
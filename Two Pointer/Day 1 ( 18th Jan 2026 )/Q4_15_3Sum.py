# problem link : https://leetcode.com/problems/3sum/description/
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k + 1
            j = n - 1

            while i < j:
                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum < 0:
                    i += 1
                elif curr_sum > 0:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])  
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
            
        return res

# -------- Main starter code --------
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]  # Example input
    solution = Solution()
    result = solution.threeSum(nums)
    print("All unique triplets that sum to 0 are:", result)

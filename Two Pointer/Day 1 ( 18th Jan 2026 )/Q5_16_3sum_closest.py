# problem link : https://leetcode.com/problems/3sum-closest/description/

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = 0

        for k in range(n - 2):
            i = k + 1
            j = n - 1

            while i < j:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    i += 1
                elif curr_sum > target:
                    j -= 1
                else:
                    return curr_sum # best and equal distance
        
        return closest_sum

# ----------- MAIN CODE -----------
if __name__ == "__main__":
    n = int(input().strip())                  # number of elements
    nums = list(map(int, input().split()))    # array elements
    target = int(input().strip())             # target value

    obj = Solution()
    print(obj.threeSumClosest(nums, target))

# problem link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            curr_sum = numbers[i] + numbers[j]

            if curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1
            else:
                return [i + 1, j + 1]  # 1-indexed as per problem statement

        return []

# -------------------------
# Example usage / main
# -------------------------
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]  # sorted input
    target = 9

    solution = Solution()
    result = solution.twoSum(numbers, target)
    print("Result:", result)  # Output: [1, 2]

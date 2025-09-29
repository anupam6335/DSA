# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/1786674308/

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k
        totalSum = sum(cardPoints)
        
        # If k == n, take all cards
        if windowSize == 0:
            return totalSum

        # Initialize sliding window
        i = 0
        currSum = 0
        minSubarraySum = float('inf')

        for j in range(n):
            currSum += cardPoints[j]

            # Maintain window of size n - k
            if j - i + 1 == windowSize:
                minSubarraySum = min(minSubarraySum, currSum)
                currSum -= cardPoints[i]
                i += 1

        return totalSum - minSubarraySum

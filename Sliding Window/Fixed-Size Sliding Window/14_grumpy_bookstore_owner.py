# https://leetcode.com/problems/grumpy-bookstore-owner/description/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        # Step 1: base satisfied
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]

        # Step 2: sliding window for extra satisfied
        i = 0
        currCnt = 0
        maxCnt = 0

        for j in range(n):
            if grumpy[j] == 1:
                currCnt += customers[j]

            # when window reaches size = minutes
            if j - i + 1 == minutes:
                maxCnt = max(maxCnt, currCnt)

                # shrink window
                if grumpy[i] == 1:
                    currCnt -= customers[i]
                i += 1

        return base + maxCnt
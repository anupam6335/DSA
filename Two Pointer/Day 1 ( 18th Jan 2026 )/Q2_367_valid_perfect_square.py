# problem link :https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        i = 1
        j = num

        while i <= j:
            mid = i + (j - i) // 2
            sq = mid * mid

            if sq < num:
                i = mid + 1
            elif sq > num:
                j = mid - 1
            else:
                return True

        return False


# ----------- MAIN CODE -----------
if __name__ == "__main__":
    num = int(input().strip())

    obj = Solution()
    print(obj.isPerfectSquare(num))

# problem Link: https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        # First convert into list because string is mutable
        s = list(s)
        n = len(s)

        def rev(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        # Remove Start leading space
        i = 0
        while i < n and s[i] == " ":
            i += 1

        # remove leading ending space
        j = n - 1
        while j >= 0 and s[j] == ' ':
            j -= 1

        # reverse complete string
        rev(i, j)
        print(s)

        # reverse each ward
        start = i
        k = i 
        while k <= j:
            if k == j or s[k + 1] == ' ':
                rev(start, k)
                start = k + 2
            k += 1
        
        print(s)
        
        # remove extra spaces and add only one space two ward
        read = i
        write = i

        while read <= j:
            if s[read] != ' ':
                s[write] = s[read] # write a char
                write += 1
            elif write > i and s[write - 1] != ' ':
                s[write] = ' ' # write only one space
                write += 1
            read += 1 
        
        return ''.join(s[i:write])

# sol = Solution()
# print("\nReturned:", sol.reverseWords("  hello   world  "))



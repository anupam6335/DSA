# Problem Link : https://neetcode.io/problems/valid-word-abbreviation/question
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n = len(word)
        m = len(abbr)
        
        while i < n and j < m:
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num 
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == n and j == m

sol = Solution()
print(sol.validWordAbbreviation("implementation","i12n"))
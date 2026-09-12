class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        total = 1
        i = 0
        j = 1
        n = len(s)
        maxTotal = total
        while j < n:
            if s[j] not in s[i:j]:
                j += 1
                total += 1
            elif s[j] in s[i:j]:
                i += 1
                total -= 1
            maxTotal = max(total, maxTotal)
        return maxTotal
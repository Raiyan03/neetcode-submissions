class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTableS = {}
        hashTableT = {}

        if len(s) != len(t):
            return False
        for i in s:
            hashTableS[i] = hashTableS.get(i, 0) + 1
        for c in t:
            hashTableT[c] = hashTableT.get(c, 0) + 1
        for i in range(len(s)):
            if hashTableS[s[i]] != hashTableT.get(s[i], 0):
                return False
        return True
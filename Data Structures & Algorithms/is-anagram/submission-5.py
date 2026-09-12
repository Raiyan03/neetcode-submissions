class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashTableS = {}
        hashTableT = {}
        
        for i in range(len(s)):
            hashTableS[s[i]] = hashTableS.get(s[i], 0) + 1
            hashTableT[t[i]] = hashTableT.get(t[i], 0) + 1
        return hashTableS == hashTableT
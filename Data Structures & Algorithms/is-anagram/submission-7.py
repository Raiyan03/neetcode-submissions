class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sn = len(s)
        tn = len(t)
        if sn != tn:
            return False

        hashS = {}
        hashT = {}

        for i in range(tn):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        
        return hashS == hashT
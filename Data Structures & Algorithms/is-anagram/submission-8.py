class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False
        for i in range(sLen):
            if s[i] not in hashS.keys():
                hashS[s[i]] = 1
            else:
                hashS[s[i]] = hashS[s[i]] + 1
            if t[i] not in hashT.keys():
                hashT[t[i]] = 1
            else:
                hashT[t[i]] = hashT[t[i]] + 1
        
        return hashS == hashT
            
        return True
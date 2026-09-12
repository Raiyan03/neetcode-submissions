class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0] * 26
        countS2 = [0] * 26
        if len(s1) > len(s2):
            return False
        a_ord = ord("a")
        for i in s1:
            countS1[ord(i) - a_ord] += 1
        
        r = len(s1)
        for i in range(r):
            countS2[ord(s2[i]) - a_ord] += 1
        
        if countS1 == countS2:
            return True
        
        l = 0
        for i in range(r, len(s2)):
            countS2[ord(s2[l]) - a_ord] -= 1
            countS2[ord(s2[i]) - a_ord] += 1
            l += 1
            if countS2 == countS1:
                return True
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {} #Declaring both the hashmaps or dictionary.
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # Using get here because it might not have that key already to avoid ket error the get method returns default value
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
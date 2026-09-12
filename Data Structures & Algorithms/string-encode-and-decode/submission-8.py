class Solution:

    def encode(self, strs: List[str]) -> str:
        outString = ""
        for s in strs:
            outString += f"{len(s)}#"+s
        return outString
        
    def decode(self, s: str) -> List[str]:
        outList = []
        i = 0
        while i < len(s):
            k = i
            sLen = 0
            while s[k] != "#":
                k += 1
            sLen = int(s[i:k]) 
            outList.append(s[ k + 1 : sLen + k + 1])
            i = k + sLen + 1
        return outList
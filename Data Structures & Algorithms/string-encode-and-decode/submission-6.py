class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        for i in strs:
            str += f"{len(i)}#{i}"
        return str
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lenght = int(s[i:j])
            res.append(s[j + 1:lenght + j + 1])
            i = lenght + j + 1
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        for s in strs:
            str += f"{len(s)}#{s}"
        print(str)
        return str
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            print(i, j)
            res.append(s[j + 1 : lenght + j + 1])
            i = lenght + j + 1
        return res
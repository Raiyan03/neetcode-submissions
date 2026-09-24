class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out = out + str(len(s)) + "#" + s
        print(out)
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        j = 0

        while i < len(s):
            if s[j] == '#':
                offset = int(s[i:j])
                start = j + 1
                end = start + offset
                out.append(s[start:end])
                i = end
                j = end + 1
            else:
                j += 1
        return out
        

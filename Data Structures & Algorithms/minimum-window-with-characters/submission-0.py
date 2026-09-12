class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        window = {}
        for i in t:
            tCount[i] = tCount.get(i, 0) + 1
            window[i] = 0

        reslen, res = float("infinity"), [-1, -1]

        l = 0
        have, need = 0, len(tCount)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            print(c)
            if c in tCount and window[c] == tCount[c]:
                print("add")
                have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r + 1]
                d = s[l]
                window[d] -= 1
                if d in t and window[d] < tCount[d]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r  = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            l, r = l + 1, r - 1
        return True
    def alphaNum(self, c):
        return  ((ord(c) in range(ord("a"), ord("z") + 1))
                or (ord(c) in range(ord("0"), ord("9") + 1))
                or (ord(c) in range(ord("A"), ord("Z") + 1)))
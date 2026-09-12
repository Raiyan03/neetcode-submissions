class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while r > l:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    
    def isAlphaNum(self, c: str) -> bool:
        return (ord(c) in range(ord('A'), ord('Z') + 1)) or (ord(c) in range(ord('a'), ord('z') + 1)) or (ord(c) in range(ord('0'), ord('9') + 1))
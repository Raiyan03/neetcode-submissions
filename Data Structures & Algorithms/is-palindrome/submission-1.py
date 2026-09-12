class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ord("a")
        z = ord("z") + 1
        O = ord("0")
        nine = ord("9") + 1
        string = s.lower()
        j = len(s) - 1
        backward = ""
        front = ""
        for i in range(len(s)):
            if ord(string[i]) in range(a, z) or ord(string[i]) in range(O, nine):
                front += string[i]
            if ord(string[j]) in range(a, z) or ord(string[j]) in range(O, nine):
                backward += string[j]
            j -= 1
        print(backward , front)
        return backward == front
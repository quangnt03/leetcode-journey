class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                if c.isalpha():
                    c = c.lower()
                chars.append(c)
        if len(chars) < 2:
            return True
        n = len(chars)
        for i in range(n // 2):
            if chars[i] != chars[n - i - 1]:
                return False
        return True
'''
n = 5
0 4 i n-i-1
1 3
2
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        basechr = ord('a')
        a = [0 for _ in range(27)]
        b = [0 for _ in range(27)]
        for i in range(len(s)):
            a[ord(s[i]) - basechr] += 1
            b[ord(t[i]) - basechr] += 1
        for i in range(27):
            if a[i] != b[i]:
                return False
        return True
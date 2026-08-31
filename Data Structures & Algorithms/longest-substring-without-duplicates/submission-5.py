class Solution:
    def hashChar(self, c: str) -> int: 
        return ord(c[0]) - ord('a')

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 0
        res = 1
        count = {}
        
        while l <= r and r < len(s):
            if r < len(s):
                count[s[r]] = count.get(s[r], 0) + 1
            else:
                break
            
            while count.get(s[r], 0) > 1:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res
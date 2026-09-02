class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what is the longest substring with only s[i] char
        # if len of current substring (0:i) == i - k + 1, then s[0]:s[i] is the target string
        l = 0
        ans = 1
        n = len(s)
        count = {}
        maxfreq = 1
        
        for r in range(n):
            count[s[r]] = count.get(s[r], 0) + 1
            maxfreq = max(maxfreq, count[s[r]])
            while r - l + 1 > maxfreq + k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            ans = max(ans, r - l + 1)
                
        return ans

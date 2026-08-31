class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        num_set = set(nums)
        max_val = max(num_set)
        max_len = 1
        for num in nums:
            if (num - 1) not in num_set:
                clen = 1
                a = num + 1
                while a in num_set:
                    clen += 1
                    a += 1 
                max_len = max(clen, max_len)
        return max_len
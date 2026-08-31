class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_len = 1
        clen = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                clen += 1
            elif nums[i] - nums[i-1] > 1:
                clen = 1
            max_len = max(clen, max_len)
        return min(max_len, len(nums))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        n = len(nums)
        for i, v in enumerate(nums):
            if (target - v) in hash:
                return [hash[(target - v)], i]
            else:
                hash[v] = i
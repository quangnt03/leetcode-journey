class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prods = [1 for _ in range(n)]
        suffix_prods = [1 for _ in range(n)]
        result = [1 for _ in range(n)]
        
        prefix_prods[0] = nums[0]
        suffix_prods[-1] = nums[-1]
        
        for i in range(1, n):
            prefix_prods[i] = prefix_prods[i-1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffix_prods[i] = suffix_prods[i + 1] * nums[i]
        for i in range(0, n):
            if i == 0:
                result[i] = suffix_prods[i + 1]
            elif i == n - 1:
                result[i] = prefix_prods[i - 1]
            else:
                result[i] = prefix_prods[i - 1] * suffix_prods[i + 1]
        return result
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        if min(nums) > 0:
            return []
            
        nums = sorted(nums)
        n = len(nums)
        ans = []
        setnum = set()
        for i in range(0, n - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            target = 0 - nums[i]
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return ans
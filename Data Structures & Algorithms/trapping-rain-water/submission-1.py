class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        water = 0
        leftmax = height[0]
        rightmax = height[r]
        
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(height[l], leftmax)
                water += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(height[r], rightmax)
                water += rightmax - height[r]
        return water
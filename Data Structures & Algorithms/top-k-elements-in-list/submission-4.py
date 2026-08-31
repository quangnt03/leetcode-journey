class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        buckets = {}
        counts = [[] for _ in range(n + 1)]
        
        for num in nums:
            buckets[num] = buckets.get(num, 0) + 1

        for key, count in buckets.items():
            counts[count].append(key)
        
        i = n
        while i >= 0 and len(ans) < k:
            sub = counts[i]
            ans.extend(sub[0 : min(len(sub), k - len(ans))])
            i -= 1
        return ans


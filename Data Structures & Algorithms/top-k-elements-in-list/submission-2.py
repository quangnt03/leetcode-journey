class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        mostCom = freqs.most_common(k)
        return [pair[0] for pair in mostCom]

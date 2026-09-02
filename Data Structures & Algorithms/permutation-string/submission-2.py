class Solution:
    def isPermutation(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1
        for c in s2:
            count_s2[c] = count_s2.get(c, 0) + 1
        
        for c in s1:
            if c not in count_s2 or count_s1[c] != count_s2[c]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1
        l = 0
        for r in range(len(s2) - len(s1) + 1):
            sub = s2[r: r + len(s1)]
            if self.isPermutation(sub, s1):
                return True

        return False
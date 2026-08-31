class Solution:
    def build_frequency_term(self, s: str) -> Tuple[int]:
        term = [0 for _ in range(26)]
        for c in list(s):
            idx = ord(c) - ord('a')
            term[idx] += 1
        return tuple(term)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        
        for s in strs:
            f_term = self.build_frequency_term(s)
            ana_group = keys.get(f_term, [])
            ana_group.append(s)
            keys[f_term] = ana_group

        ans = list(keys.values())

        return ans

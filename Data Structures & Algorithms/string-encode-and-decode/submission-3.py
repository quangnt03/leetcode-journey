class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += f'{len(s)}@{s}'
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            num_char = ''
            while i < len(s) and s[i] != '@':
                num_char += s[i]
                i += 1
            cs = ''
            i += 1    
            char_len = int(num_char)
            
            for _ in range(char_len):
                cs += s[i]
                i += 1
            result.append(cs)
        return result
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapping = Counter(s)
        result = []
        
        for ch in order:
            if ch in mapping:
                result.append(ch * mapping[ch])
                del mapping[ch]
        
        for ch, count in mapping.items():
            result.append(ch * count)

        return "".join(result)

        
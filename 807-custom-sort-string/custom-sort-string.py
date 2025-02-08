class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time: O(N), where N is length of order
        Space: O(M + N), where M is the length of s and N is the length of order
        """
        mapping = Counter(s)
        result = []
        
        for ch in order:
            if ch in mapping:
                result.append(ch * mapping[ch])
                del mapping[ch]
        
        for ch, count in mapping.items():
            result.append(ch * count)

        return "".join(result)

        
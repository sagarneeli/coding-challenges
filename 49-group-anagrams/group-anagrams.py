class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            char_count = [0] * 26
            for ch in string:
                char_count[ord(ch) - ord("a")] += 1
            mapping[tuple(char_count)].append(string)
        
        return list(mapping.values())

        
        
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix_count = [0] * (len(words) + 1)
        prev_count = 0

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prev_count += 1
            prefix_count[i + 1] = prev_count
        
        result = [0] * len(queries)
        
        for i, query in enumerate(queries):
            l, r = query
            result[i] = prefix_count[r + 1] - prefix_count[l]
        
        return result
        

        
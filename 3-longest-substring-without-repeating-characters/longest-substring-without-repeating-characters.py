class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = defaultdict(int)
        max_length = 0
        start, end = 0, 0

        while end < len(s):
            ch = s[end]
            if ch in char_map:
                start = max(start, char_map[ch] + 1)
            
            max_length = max(max_length, end - start + 1)
            char_map[ch] = end
            end += 1
    
        return max_length

            

            
        
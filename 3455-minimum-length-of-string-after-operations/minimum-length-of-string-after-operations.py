class Solution:
    def minimumLength(self, s: str) -> int:
        char_freq = Counter(s)
        delete_count = 0

        for freq in char_freq.values():
            if freq % 2 == 1:
                delete_count += freq - 1
            else:
                delete_count += freq - 2
        
        return len(s) - delete_count
        
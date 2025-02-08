class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for ch, freq in ransom_count.items():
            if magazine_count[ch] < freq:
                return False

        return True
        
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtrack():
            result = 0

            for ch in count:
                if count[ch] > 0:
                    count[ch] -= 1
                    result += 1
                    result += backtrack()
                    count[ch] += 1
            
            return result
        
        return backtrack()
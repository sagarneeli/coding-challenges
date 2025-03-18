class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(string, index, path):
            if index == len(string):
                print(path)
                result.append(" ".join(path))
                return
            
            for end in range(index + 1, len(string) + 1):
                word = string[index: end]
                if word in wordDict:
                    path.append(word)
                    backtrack(string, end, path)
                    path.pop()

        result = []
        backtrack(s, 0, [])
        return result
        
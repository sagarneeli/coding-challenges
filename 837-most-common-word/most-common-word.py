class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = paragraph.split()
        words_count = Counter(words)
        max_count = 0

        result = ""
        print(words_count)
        for word, count in words_count.items():
            if word in banned:
                continue
            print(word)
            print(count)
            print(max_count)
            if count > max_count:
                result = word
                max_count = count
            print(max_count)
            print(result)
        
        return result

        
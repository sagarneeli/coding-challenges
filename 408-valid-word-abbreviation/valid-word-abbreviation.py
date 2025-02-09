class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, count = 0, 0
        while i < len(abbr):
            if abbr[i] == "0" or count >= len(word):
                return False

            number = ""
            while i < len(abbr) and abbr[i].isdigit():
                number += abbr[i]
                i += 1
            
            if number:
                count += int(number)
            else:
                if abbr[i] != word[count]:
                    return False
                count += 1
                i += 1

        return count == len(word)

        
        
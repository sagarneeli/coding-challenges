class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def is_match(string):
            M = len(string)
            N = len(pattern)
            
            if M < N:
                return False

            i, j = 0, 0
            while i < M and j < N:
                print(string[i])
                print(pattern[j])
                if string[i] == pattern[j]:
                    i += 1
                    j += 1
                elif string[i].islower():
                    i += 1
                else:
                    return False
            
            if j < N:
                return False

            while i < M:
                if string[i].islower():
                    i += 1
                else:
                    return False
            
            return True
        
        result = []
        for query in queries:
            result.append(is_match(query))
        
        return result
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Step 1: Find the potential celebrity candidate
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1

        return candidate

        
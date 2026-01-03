class Solution:
    def numOfWays(self, n: int) -> int:
        # Initialize counts for the two valid row patterns:
        # - typeA: ABA pattern (first and third cells same)
        # - typeB: ABC pattern (all three cells different)
        typeA = 6
        typeB = 6
        MOD = 10**9 + 7
        
        # Iterate from the second row to the nth row
        for i in range(2, n + 1):
            # Compute new counts based on valid transitions from previous row types
            new_typeA = (3 * typeA + 2 * typeB) % MOD
            new_typeB = (2 * typeA + 2 * typeB) % MOD
            
            # Update counts for current row
            typeA, typeB = new_typeA, new_typeB
        
        # Return total number of valid colorings modulo MOD
        return (typeA + typeB) % MOD
"""
https://leetcode.com/problems/number-of-1-bits/ - Count number of 1's
Solution reference - https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

Returns:
    [type]: [int]

Time Complexity - O(1)
Space Complexity - O(1)

Brian Kernighan’s Algorithm - Bit shift optimization
- Turn off the rightmost 1 bit in each iteration
- To achieve this we perform the operation - num & (num - 1)
- As we flip the bit we will also increment the count.

Example:

  0101 (5)
& 0100 (4)
-----------
  0100 (4)

count = 1

num > 0, continue 

  0100 (4)
& 0100 (3)
-----------
  0000 (0)

count = 2

num == 0, loop breaks and return count
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

class Solution:
    def coloredCells(self, n: int) -> int:
        num_blue_cells = 1
        addend = 4

        # Iterate n - 1 times
        while n - 1:

            # Add and update current multiple of 4
            num_blue_cells += addend
            addend += 4
            n -= 1

        return num_blue_cells
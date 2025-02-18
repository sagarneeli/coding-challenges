class Solution:
    def smallestNumber(self, pattern: str) -> str:
        return str(self.find_smallest_number(pattern, 0, 0, 0))

    # Recursively find the smallest number that satisfies the pattern
    def find_smallest_number(
        self,
        pattern: str,
        current_position: int,
        used_digits_mask: int,
        current_num: int,
    ) -> int:
        # Base case: return the current number when the whole pattern is processed
        if current_position > len(pattern):
            return current_num

        result = float("inf")
        last_digit = current_num % 10
        should_increment = (
            current_position == 0 or pattern[current_position - 1] == "I"
        )

        # Try all possible digits (1 to 9) that are not yet used and follow the pattern
        for current_digit in range(1, 10):
            if (used_digits_mask & (1 << current_digit)) == 0 and (
                current_digit > last_digit
            ) == should_increment:
                result = min(
                    result,
                    self.find_smallest_number(
                        pattern,
                        current_position + 1,
                        used_digits_mask | (1 << current_digit),
                        current_num * 10 + current_digit,
                    ),
                )

        return result
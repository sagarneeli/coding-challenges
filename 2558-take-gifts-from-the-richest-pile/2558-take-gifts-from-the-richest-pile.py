class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = len(gifts)

        # Create a copy of the gifts array and sort it
        sorted_gifts = sorted(gifts)

        # Perform the operation k times
        for _ in range(k):
            max_element = sorted_gifts[-1]
            sorted_gifts.pop()

            # Find the index where the square root of max_element should be inserted
            spot_of_sqrt = next(
                (
                    i
                    for i, value in enumerate(sorted_gifts)
                    if value > math.floor(math.sqrt(max_element))
                ),
                n,
            )

            # Insert the square root value at the correct position
            sorted_gifts.insert(
                spot_of_sqrt, math.floor(math.sqrt(max_element))
            )

        # Calculate the sum of the remaining elements in the sorted array
        number_of_remaining_gifts = sum(sorted_gifts)

        return number_of_remaining_gifts
        
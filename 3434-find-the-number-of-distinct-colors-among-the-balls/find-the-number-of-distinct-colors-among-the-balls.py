from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """Processes queries to find the number of distinct colors among balls.

        Args:
            limit (int): The limit.
            queries (List[List[int]]): A list of queries.

        Returns:
            List[int]: A list of results.
        """
        ball_map = defaultdict(int)
        color_map = defaultdict(int)
        result = []

        for query in queries:
            ball, color = query

            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1
                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            ball_map[ball] = color
            color_map[color] += 1

            result.append(len(color_map))

        return result

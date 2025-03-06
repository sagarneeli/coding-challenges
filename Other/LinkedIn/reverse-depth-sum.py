# Assuming the NestedInteger class in Python looks like this:
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         Return True if this NestedInteger holds a single integer,
#         rather than a nested list.
#         """
#         ...
#
#     def getInteger(self) -> int:
#         """
#         Return the single integer that this NestedInteger holds,
#         if it holds a single integer.
#         Otherwise, return None.
#         """
#         ...
#
#     def getList(self) -> [NestedInteger]:
#         """
#         Return the nested list if this NestedInteger holds a nested list.
#         Return an empty list if this NestedInteger holds a single integer.
#         """
#         ...

from typing import List


class Solution:
    def reverseDepthSum(self, nestedList: List["NestedInteger"]) -> int:
        """
        Returns the "reverse depth sum" of the nested list, where
        outermost integers have the highest weight, and deeper integers
        have lower weights.
        """
        unweighted = 0
        weighted = 0
        current_level = nestedList

        # Process the list level by level.
        while current_level:
            next_level = []
            for ni in current_level:
                if ni.isInteger():
                    # Add all integers at the current level to unweighted.
                    unweighted += ni.getInteger()
                else:
                    # Flatten nested lists into the next level.
                    next_level.extend(ni.getList())

            # Each level's sum gets added to weighted.
            # Outer levels accumulate multiple times,
            # matching the "reverse depth" weighting.
            weighted += unweighted
            current_level = next_level

        return weighted

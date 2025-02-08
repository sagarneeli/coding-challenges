"""
From string s, find all the substrings of size k with exactly (k-1) unique characters
(in other words, exactly 1 duplicated character).
Print the starting index of the valid substrings.
Expected time complexity O(n) instead of O(n * k)
Input
s = "iraceacar"
k = 5
Expected output
[1, 4]
substrings with (k - 1) unique chars are
1: "racea", 4: "eacar" AOneCo
"""


def find_substrings(s, k):
    n = len(s)
    result = []

"""
2916. Subarrays Distinct Element Sum of Squares II  (Hard, daily 2026-10-16)
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

Return the sum of the squares of the distinct counts of all subarrays of nums,
modulo 10^9 + 7. Same as 2913, but O(n^2) is too slow at this size.
Constraints: 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^5
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        pass


N = 10**5

CASES = [
    # LeetCode examples
    (([1, 2, 1],), 15),
    (([2, 2],), 3),
    # edge cases
    (([1],), 1),
    (([1, 2, 3],), 20),
    (([1, 2, 2, 1],), 25),
    (([3, 1, 3, 2],), 38),
    # max length (answers are mod 10^9 + 7): all distinct, all equal, repeating pattern
    ((list(range(1, N + 1)),), 497683716),
    (([7] * N,), 49965),
    (([i % 10 + 1 for i in range(N)],), 943498367),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    assert Solution().sumCounts(*args) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().sumCounts(*args)
        shown = args if len(args[0]) <= 10 else f"(<{len(args[0])} items>,)"
        print("PASS" if got == expected else "FAIL", shown, "->", got, "| expected", expected)

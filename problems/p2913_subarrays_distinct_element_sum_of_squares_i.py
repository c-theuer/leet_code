"""
2913. Subarrays Distinct Element Sum of Squares I
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

Return the sum of the squares of the distinct counts of all subarrays of nums.
Constraints: 1 <= nums.length <= 100, 1 <= nums[i] <= 100
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                distinct = set()
                distinct.add(nums[j])
                res += len(distinct)

        return res


CASES = [
    # LeetCode examples
    (([1, 2, 1],), 15),
    (([1, 1],), 3),
    # edge cases
    (([1],), 1),
    (([2, 2, 2],), 6),
    (([1, 2, 3],), 20),
    (([1, 2, 2, 1],), 25),
    (([3, 1, 3, 2],), 38),
    # max length: all distinct, all equal, repeating pattern
    ((list(range(1, 101)),), 8670850),
    (([7] * 100,), 5050),
    (([i % 10 + 1 for i in range(100)],), 445360),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    assert Solution().sumCounts(*args) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().sumCounts(*args)
        shown = args if len(args[0]) <= 10 else f"(<{len(args[0])} items>,)"
        print(
            "PASS" if got == expected else "FAIL",
            shown,
            "->",
            got,
            "| expected",
            expected,
        )

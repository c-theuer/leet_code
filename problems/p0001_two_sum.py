"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []


CASES = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    assert Solution().twoSum(*args) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().twoSum(*args)
        print("PASS" if got == expected else "FAIL", args, "->", got, "| expected", expected)

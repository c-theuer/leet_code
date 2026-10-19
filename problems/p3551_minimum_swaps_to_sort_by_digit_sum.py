"""
3551. Minimum Swaps to Sort by Digit Sum  (Medium, daily 2026-10-17)
https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

nums holds distinct positive integers. Sort by digit sum ascending, breaking ties
by the smaller number first. Return the minimum number of swaps (exchanging the
values at two distinct positions) needed to reach that order.
Constraints: 1 <= nums.length <= 10^5, 1 <= nums[i] <= 10^9, nums is distinct
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        digit_sums = [None] * len(nums)
        total_swaps = 0

        for i in range(len(nums)):
            new_digit_sum = self.digit_sum(nums[i])
            new_digit_sum_index = i

            while new_digit_sum_index > 0 and (
                digit_sums[new_digit_sum_index - 1] > new_digit_sum
                or digit_sums[new_digit_sum_index - 1] == new_digit_sum
                and nums[new_digit_sum_index - 1] > nums[i]
            ):
                digit_sums[new_digit_sum_index] = digit_sums[new_digit_sum_index - 1]
                digit_sums[new_digit_sum_index - 1] = None
                new_digit_sum_index -= 1

            digit_sums[new_digit_sum_index] = new_digit_sum
            total_swaps += i - new_digit_sum_index

        return total_swaps

    def digit_sum(self, n: int) -> int:
        return sum(int(c) for c in str(n))


N = 10**5

CASES = [
    # LeetCode examples
    (([37, 100],), 1),
    (([22, 14, 33, 7],), 0),
    (([18, 43, 34, 16],), 2),
    # edge cases
    (([5],), 0),
    (([1, 10, 100],), 0),  # all digit sum 1, already in value order
    (([100, 10, 1],), 3),  # all digit sum 1, tie-break decides
    (([3, 1, 2],), 2),  # one 3-cycle
    (([19, 28, 91, 10**9],), 3),  # one 4-cycle
    (([999_999_999, 1],), 1),  # largest digit sum vs smallest
    # max length
    ((list(range(1, N + 1)),), 99988),
    ((list(range(N, 0, -1)),), 99988),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    # Copy the input so a solution that mutates nums can't affect other runs.
    assert Solution().minSwaps(list(args[0])) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().minSwaps(list(args[0]))
        shown = args if len(args[0]) <= 10 else f"(<{len(args[0])} items>,)"
        print(
            "PASS" if got == expected else "FAIL",
            shown,
            "->",
            got,
            "| expected",
            expected,
        )

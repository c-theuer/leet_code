"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Return the kth largest element in nums (in sorted order, not the kth distinct).
Can you solve it without sorting?
Constraints: 1 <= k <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4
"""

import random

import pytest
import heapq

from lc import *  # noqa: F401,F403


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)

        for i in range(k - 1):
            heapq.heappop_max(nums)

        return heapq.heappop_max(nums)


# Max-length input: every value in -10^4..10^4 four or five times (10000 appears
# exactly 4 times), in a fixed shuffled order.
BIG = [i % 20001 - 10000 for i in range(100000)]
random.Random(0).shuffle(BIG)

CASES = [
    # LeetCode examples
    (([3, 2, 1, 5, 6, 4], 2), 5),
    (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    # edge cases
    (([1], 1), 1),
    (([2, 1], 1), 2),
    (([2, 1], 2), 1),
    (([5, 5, 5, 5], 3), 5),
    (([-1, -1, -2], 2), -1),
    (([-10000, 10000, 0], 3), -10000),
    (([7, 6, 5, 4, 3, 2, 1], 7), 1),
    # max length: largest, just past the duplicated max, median, smallest
    ((BIG, 1), 10000),
    ((BIG, 5), 9999),
    ((BIG, 50000), 0),
    ((BIG, 100000), -10000),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    # Copy the input so a solution that mutates nums can't affect other runs.
    nums, k = args
    assert Solution().findKthLargest(list(nums), k) == expected


if __name__ == "__main__":
    for (nums, k), expected in CASES:
        got = Solution().findKthLargest(list(nums), k)
        shown = (nums, k) if len(nums) <= 10 else (f"<{len(nums)} items>", k)
        print(
            "PASS" if got == expected else "FAIL",
            shown,
            "->",
            got,
            "| expected",
            expected,
        )

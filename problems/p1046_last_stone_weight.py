"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

Repeatedly smash the two heaviest stones x <= y: if x == y both are destroyed,
otherwise y becomes y - x. Return the weight of the last stone, or 0 if none remain.
Constraints: 1 <= stones.length <= 30, 1 <= stones[i] <= 1000
"""

import pytest
import heapq

from lc import *  # noqa: F401,F403


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if x < y:
                heapq.heappush_max(stones, y - x)

        return stones.pop() if len(stones) == 1 else 0


CASES = [
    # LeetCode examples
    (([2, 7, 4, 1, 8, 1],), 1),
    (([1],), 1),
    # edge cases
    (([2, 2],), 0),
    (([3, 7],), 4),
    (([1, 1, 1],), 1),
    (([10, 4, 2, 10],), 2),
    # max length
    (([1000] * 30,), 0),
    ((list(range(1, 31)),), 1),
    (([1000] + [1] * 29,), 971),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    # Copy the input so a solution that mutates stones can't affect other runs.
    assert Solution().lastStoneWeight(list(args[0])) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().lastStoneWeight(list(args[0]))
        shown = args if len(args[0]) <= 10 else f"(<{len(args[0])} items>,)"
        print(
            "PASS" if got == expected else "FAIL",
            shown,
            "->",
            got,
            "| expected",
            expected,
        )

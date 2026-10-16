"""
<number>. <Title>
https://leetcode.com/problems/<slug>/

Copy to problems/p<number>_<slug>.py, paste the LeetCode signature, fill in CASES.
Run/debug with F5 ("Debug current problem"), or run the tests from the Testing panel.
"""

import pytest

from lc import *  # noqa: F401,F403  ListNode, TreeNode, build_list, build_tree, List, Optional...


class Solution:
    def solve(self, nums: List[int]) -> int:
        pass


CASES = [
    # (input args tuple, expected)
    (([1, 2, 3],), 0),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    assert Solution().solve(*args) == expected


if __name__ == "__main__":
    # Set breakpoints anywhere above, then press F5.
    for args, expected in CASES:
        got = Solution().solve(*args)
        print("PASS" if got == expected else "FAIL", args, "->", got, "| expected", expected)

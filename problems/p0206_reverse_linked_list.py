"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


CASES = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
]


@pytest.mark.parametrize("values, expected", CASES)
def test_solution(values, expected):
    assert list_to_array(Solution().reverseList(build_list(values))) == expected


if __name__ == "__main__":
    for values, expected in CASES:
        got = list_to_array(Solution().reverseList(build_list(values)))
        print("PASS" if got == expected else "FAIL", values, "->", got, "| expected", expected)
